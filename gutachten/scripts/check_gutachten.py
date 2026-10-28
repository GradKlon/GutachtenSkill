#!/usr/bin/env python3
"""Formale Prüfung juristischer Gutachten in Markdown.

Meldet Verstöße gegen Gutachtenstil, Zitierweise und Fußnotenregeln und zählt die Zeichen des
Fließtexts (ohne Überschriften und Fußnoten). Die Treffer sind Heuristiken und im Kontext zu
beurteilen.

Aufruf: python3 check_gutachten.py [--ohne-zitierweise] [--zeilenlaenge N] datei.md [...]
"""
import argparse
import re
import sys

HEAD_OK = re.compile(r"^#{1,6} (Teil \d|Frage \d|Fall \d|Abwandlung|[A-H]\.|[IVX]+\.|\d+\.|[a-z]\)|[a-z]{2}\)|\(\d+\))")
URTEILSSTIL = [
    r"scheidet[^.]{0,30} aus, (weil|da)\b",
    r"liegt[^.]{0,30} (nicht )?vor, (weil|da)\b",
    r"ist[^.]{0,20} zu (verneinen|bejahen), (weil|da)\b",
    r"^(Ein|Eine|Der|Die|Das) [^.]{0,60} (scheitert|entfällt|greift nicht)[^.]{0,10}, (weil|da)\b",
    r"\b(unproblematisch|offensichtlich|unstreitig|selbstverständlich)\b",
]
AUTORITAET = re.compile(r"\b(BGH|BVerfG|BAG|BFH|BSG|BVerwG|EuGH|OLG|KG|LG|AG|RG)\b")
ERGEBNIS_FN = re.compile(r"\b(somit|folglich|daher|demnach)\b[^.]*\.?\[\^\d+\]")


def pruefe(pfad, zitierweise=True, zeilenlaenge=None):
    text = open(pfad, encoding="utf-8").read()
    zeilen = text.split("\n")
    hinweise = []
    im_code = False
    fliesstext = []

    for nr, z in enumerate(zeilen, 1):
        if z.startswith("```"):
            im_code = not im_code
            continue
        if im_code or z.startswith("|") or z.startswith(">"):
            continue
        ist_fn = z.startswith("[^")
        ist_ueberschrift = z.startswith("#")

        if ist_ueberschrift and not HEAD_OK.match(z):
            hinweise.append((nr, "Überschrift ohne Nummer", z))
        if re.match(r"^\s*([-*+]|\d+\.)\s", z):
            hinweise.append((nr, "Listenmarker", z))
        if re.match(r"^\s*\*\*[^*]+\.\*\*\s", z):
            hinweise.append((nr, "Fettetikett statt Überschrift", z[:80]))
        if zeilenlaenge and len(z) > zeilenlaenge and not ist_fn:
            hinweise.append((nr, f"Zeile > {zeilenlaenge}", z[:60]))

        if zitierweise:
            if re.search(r"\bAbs\.", z):
                hinweise.append((nr, "„Abs.“ statt römischer Ziffer", z.strip()[:120]))
            if re.search(r"(?<!EG)BGB\b", z):
                hinweise.append((nr, "„BGB“ hinter BGB-Norm", z.strip()[:120]))
            if not ist_fn and re.search(r"\((?:§|Art\.)", z):
                hinweise.append((nr, "Norm in Klammern", z.strip()[:120]))

        if ist_fn or ist_ueberschrift:
            continue
        fliesstext.append(z)
        for muster in URTEILSSTIL:
            if re.search(muster, z):
                hinweise.append((nr, "Urteilsstil?", z.strip()[:120]))
        if AUTORITAET.search(z):
            hinweise.append((nr, "Gerichtsname im Fließtext", z.strip()[:120]))
        if ";" in z:
            hinweise.append((nr, "Semikolon", z.strip()[:120]))
        if ERGEBNIS_FN.search(z):
            hinweise.append((nr, "Fußnote an Ergebnissatz?", z.strip()[:120]))

    refs = re.findall(r"\[\^(\d+)\](?!:)", text)
    defs = re.findall(r"^\[\^(\d+)\]:", text, re.M)
    if set(refs) != set(defs):
        fehlend = sorted(set(refs) - set(defs), key=int)
        ueberzaehlig = sorted(set(defs) - set(refs), key=int)
        hinweise.append((0, "Fußnoten", f"ohne Text: {fehlend}, ohne Verweis: {ueberzaehlig}"))
    reihenfolge = [int(x) for x in dict.fromkeys(refs)]
    if reihenfolge != list(range(1, len(reihenfolge) + 1)):
        hinweise.append((0, "Fußnotenreihenfolge", str(reihenfolge)))

    roh = re.sub(r"\[\^\d+\]", "", " ".join(z for z in fliesstext if z.strip()))
    zeichen = len(re.sub(r"\s+", " ", roh).strip())
    return zeichen, len(set(defs)), hinweise


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("dateien", nargs="+")
    ap.add_argument("--ohne-zitierweise", action="store_true",
                    help="Prüfungen zu „Abs.“, „BGB“ und Normen in Klammern abschalten")
    ap.add_argument("--zeilenlaenge", type=int, default=None,
                    help="Zeilen über dieser Länge melden")
    args = ap.parse_args()

    gesamt = 0
    alle = 0
    for pfad in args.dateien:
        zeichen, fn, hinweise = pruefe(pfad, not args.ohne_zitierweise, args.zeilenlaenge)
        gesamt += zeichen
        alle += len(hinweise)
        print(f"== {pfad}: {zeichen} Zeichen Text, {fn} Fußnoten, {len(hinweise)} Hinweise")
        for nr, art, auszug in hinweise:
            print(f"   Z. {nr:>4}  {art}: {auszug}")
    if len(args.dateien) > 1:
        print(f"GESAMT: {gesamt} Zeichen Text, {alle} Hinweise")
    sys.exit(1 if alle else 0)


if __name__ == "__main__":
    main()
