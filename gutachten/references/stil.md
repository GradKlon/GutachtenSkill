# Gutachtenstil: Regeln mit Beispielen

Die Beispiele verwenden einen neutralen Lehrbuchfall (V verkauft K ein gebrauchtes Fahrrad für 500 €)
und Platzhalter statt echter Fundstellen.

## 1. Der Vierschritt

Jeder Prüfungspunkt besteht aus Obersatz, Definition oder Maßstab, Subsumtion und Ergebnis.

Der Obersatz formuliert die zu prüfende Rechtsfolge als Möglichkeit (Konjunktiv) und nennt, wo es
nicht selbstverständlich ist, den Anlass der Prüfung. Die Definition oder der Maßstab sagt, was das
Tatbestandsmerkmal verlangt. Die Subsumtion ordnet die Sachverhaltsangaben dem Maßstab zu. Das
Ergebnis folgt daraus und wird erst am Ende ausgesprochen.

Gut:

> V könnte gegen K einen Anspruch auf Zahlung von 500 € gem. § 433 II haben. Dazu müssten V und K
> einen wirksamen Kaufvertrag geschlossen haben. Ein Vertrag kommt durch zwei übereinstimmende
> Willenserklärungen, Angebot und Annahme, zustande.[^1] V bot K das Fahrrad am Montag für 500 € an,
> K erklärte daraufhin, er nehme das Angebot an. Ein Kaufvertrag ist somit geschlossen.

Schlecht (Urteilsstil, Ergebnis vorweg):

> Ein Anspruch aus § 433 II besteht, weil V und K einen Kaufvertrag geschlossen haben.

## 2. Anlass im Obersatz

Wird ein Punkt geprüft, weil der Sachverhalt einen Hinweis gibt, gehört dieser Hinweis in den
Obersatz. Sonst wirkt die Prüfung beliebig.

Gut:

> Der Kaufvertrag könnte jedoch gem. § 142 I als von Anfang an nichtig anzusehen sein, weil K ihn mit
> der Begründung angefochten hat, V habe einen Unfallschaden verschwiegen.

Schlecht:

> Der Vertrag könnte nichtig sein.

## 3. Auch Unproblematisches im Gutachtenstil

Unproblematische Punkte werden kurz, aber im Gutachtenstil behandelt. Ein Satz Obersatz, ein Satz
Maßstab mit Subsumtion, ein Ergebnis mit „somit“ genügt.

Gut:

> K müsste die Anfechtung gegenüber V erklärt haben, § 143 I. K schrieb V, er wolle „von dem Geschäft
> nichts mehr wissen“. Darin liegt eine Anfechtungserklärung gegenüber dem Anfechtungsgegner.

Typische Urteilsstil-Formeln, die vermieden werden: „scheidet aus, weil“, „liegt vor, da“, „ist zu
bejahen, weil“, „unproblematisch“, „offensichtlich“, „unstreitig“, „selbstverständlich“.

## 4. Fließtext statt Struktur-Krücken

Das Gutachten enthält keine Stichpunktlisten, auch nicht in Vorbemerkungen, Hinweisen oder
Stellungnahmen. Aufzählungen werden ausformuliert („Erstens … Zweitens …“ oder als Satzfolge).

Keine fett gesetzten Laufüberschriften:

> **Grundsatz.** Die Anfechtung wirkt zurück …

Stattdessen eine nummerierte Überschrift in eigener Zeile:

```
##### a) Rückwirkung der Anfechtung

Die Anfechtung wirkt gem. § 142 I zurück …
```

## 5. Nummerierte Überschriften

Jede Überschrift trägt eine Nummer. Ebenenfolge: Teil/Frage → A. → I. → 1. → a) → aa) → (1).
Unnummerierte Überschriften wie „Vorbemerkung“ werden vermieden oder als eigener Gliederungspunkt
nummeriert. In Markdown entspricht die Ebene der Anzahl der `#`.

## 6. Meinungsstreit

Ein Streit wird nur entschieden, wenn es auf ihn ankommt. Kommen die Ansichten zum selben Ergebnis,
wird das festgestellt und die Entscheidung offengelassen. Kommt es darauf an, folgt auf die
Darstellung der Ansichten (jede mit Beleg) eine Stellungnahme mit eigenen Sachargumenten.

In der Stellungnahme stehen keine Gerichtsnamen und keine Autoritätsverweise. Schlecht:

> Der BGH hat diese Auffassung zu Recht abgelehnt.[^2]

Gut (die Begründung des Gerichts als eigenes Argument, belegt in der Fußnote):

> Gegen diese Auffassung spricht, dass sie dem Käufer das Risiko eines Mangels aufbürdet, den allein
> der Verkäufer erkennen konnte.[^2]

Statt Semikolons zwei Sätze oder „und“ verwenden.

## 7. Zitierweise von Normen

| Statt | Schreibe |
|---|---|
| § 123 Abs. 2 S. 1 BGB | § 123 II 1 |
| (§ 985 BGB) | gem. § 985 |
| §§ 929 S. 1, 930 BGB | §§ 929 S. 1, 930 |
| § 377 Abs. 1 HGB | § 377 I HGB |

Hat eine Norm nur einen Absatz, bleibt „S.“ stehen (§ 929 S. 1). Normen werden nicht in Klammern
gesetzt, sondern mit „gem.“, „iSv“, „iVm“ oder als Satzsubjekt eingebaut.

## 8. Fußnotenplatzierung

Fußnoten stehen an Definitionen und Maßstabssätzen, an Ansichten im Meinungsstreit und an
Stand-Vermerken. Sie stehen fast nie an Subsumtions- oder Ergebnissätzen. Fehlt ein Maßstabssatz, der
eine Fußnote tragen könnte, wird er formuliert.

Schlecht:

> K durfte daher auf die Angabe vertrauen.[^3]

Gut:

> Ein schutzwürdiges Vertrauen setzt voraus, dass der Erklärungsempfänger die Unrichtigkeit weder
> kannte noch kennen musste.[^3] K konnte den Schaden bei der Probefahrt nicht erkennen und durfte
> daher auf die Angabe vertrauen.

## 9. Anpassung

Zitierweise und Gliederungsschema sind Hausregeln eines Lehrstuhls. Verlangt ein anderer
Auftraggeber „§ 123 Abs. 2 S. 1 BGB“ oder eine andere Ebenenfolge, gilt dessen Vorgabe. Dann die
Prüfungen „Abs.“, „BGB“ und „Norm in Klammern“ im Skript mit `--ohne-zitierweise` abschalten.

[^1]: Kommentar zu § 145, Rn. (Platzhalter).
[^2]: Gericht, Datum, Aktenzeichen, Rn. (Platzhalter).
[^3]: Kommentar zu § 123, Rn. (Platzhalter).
