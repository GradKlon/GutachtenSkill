# Gutachten-Skill für Claude

Ein [Claude Skill](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview), der
Claude beibringt, zivilrechtliche Gutachten so zu schreiben, wie sie für den universitären Kontext
erwartet werden: aus dem Sachverhalt entwickelt, streng im Gutachtenstil, mit konsistenten Weichen
und ausschließlich geprüften Fundstellen. Dazu gehört ein kleines Prüfskript, das Stil- und
Zitierfehler automatisch findet.

## Aufbau

```
gutachten/
├── SKILL.md                    Einstieg: Arbeitsablauf und Kernregeln
├── references/
│   ├── stil.md                 Gutachtenstil und Zitierweise mit Gut/Schlecht-Beispielen
│   ├── belege.md               Belegpraxis gegen erfundene und falsch zugeordnete Zitate
│   └── arbeitsablauf.md        Die acht Phasen im Detail
├── assets/
│   ├── weichen-memo.md         Vorlage für das Weichen-Memo
│   └── belegliste.md           Vorlage für die Belegliste mit Prüfstatus
└── scripts/
    └── check_gutachten.py      Linter für Stil, Zitierweise, Fußnoten und Zeichenzahl
beispiel/
├── vorher.md                   Typische KI-Lösung mit 19 Befunden
└── nachher.md                  Dieselbe Prüfung im Gutachtenstil, 0 Befunde
```

`SKILL.md` ist bewusst kurz gehalten. Die Detailregeln liegen in `references/` und werden nur geladen,
wenn Claude sie braucht (Progressive Disclosure), damit der Kontext nicht unnötig belastet wird.

## Installation

Für Claude Code den Ordner `gutachten/` in das Skill-Verzeichnis kopieren, entweder global oder für
ein Projekt:

```bash
cp -r gutachten ~/.claude/skills/
```

In der Claude-App den Ordner `gutachten/` als ZIP packen und in den Einstellungen im Bereich
Skills hochladen. Claude lädt den Skill automatisch, sobald es um ein Gutachten, eine Hausarbeit oder
eine Klausurlösung geht.

## Nutzung

Beispiele für Aufträge:

> Löse den Sachverhalt in `sachverhalt.md` als Gutachten. Fang mit dem Weichen-Memo an.

> Prüfe `frage3.md` auf Gutachtenstil und Zitierweise.

> Mach mir Kürzungsvorschläge für Frage 2, insgesamt etwa 5.000 Zeichen.

Das Prüfskript funktioniert auch ohne Claude:

```bash
python3 gutachten/scripts/check_gutachten.py beispiel/vorher.md beispiel/nachher.md
```

```
== beispiel/vorher.md: 457 Zeichen Text, 1 Fußnoten, 19 Hinweise
   Z.    3  „Abs.“ statt römischer Ziffer: ## Anspruch V gegen K (§ 433 Abs. 2 BGB)
   Z.    5  Fettetikett statt Überschrift: **Vertragsschluss.** Ein Kaufvertrag liegt vor, da …
   Z.    5  Urteilsstil?: **Vertragsschluss.** Ein Kaufvertrag liegt vor, da V und K …
   Z.    8  Gerichtsname im Fließtext: … Der BGH hat
   Z.   12  Listenmarker: - Anfechtungserklärung: (+)
   …
== beispiel/nachher.md: 1858 Zeichen Text, 2 Fußnoten, 0 Hinweise
```

Mit `--ohne-zitierweise` lassen sich die lehrstuhlspezifischen Zitierregeln abschalten, mit
`--zeilenlaenge N` werden überlange Zeilen gemeldet.

## Grenzen

Der Skill ersetzt keine juristische Prüfung. Er verhindert erfundene Fundstellen nicht technisch,
sondern über einen Arbeitsablauf, der jede Fußnote einem Prüfstatus zuordnet und die Prüfung in einer
Datenbank wie beck-online oder juris beim Menschen lässt. Das Skript arbeitet mit Heuristiken und
meldet auch Fälle, die im Kontext korrekt sind. Zitierweise und Gliederungsschema folgen den Vorgaben
eines Lehrstuhls und sind in `references/stil.md` anpassbar.
