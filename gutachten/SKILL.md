---
name: gutachten
description: Erstellt, überarbeitet und prüft juristische Gutachten (Hausarbeiten, Klausurlösungen, Musterlösungen) im deutschen Zivilrecht im strengen Gutachtenstil. Verwenden, wenn ein Sachverhalt gelöst, eine Lösungsskizze ausformuliert, ein Gutachten korrigiert oder auf Stil, Zitierweise und Belege geprüft werden soll. Auslöser sind etwa „Gutachten“, „Hausarbeit“, „Klausur lösen“, „Musterlösung“, „Lösungsskizze“, „Gutachtenstil“, „Anspruchsprüfung“ oder „Fall lösen“.
---

# Juristisches Gutachten

Dieser Skill führt durch die Erstellung eines zivilrechtlichen Gutachtens, das wie eine sehr gute
Hausarbeit aussieht: aus dem Sachverhalt entwickelt, streng im Gutachtenstil, mit tragfähigen
Weichen und ausschließlich geprüften Belegen.

Die Regeln stammen aus einem langen Praxisprojekt (Musterlösung für eine Hausarbeit, vier Fassungen).
Die beiden wichtigsten Erkenntnisse daraus sind:

1. **Gutachten scheitern an unstimmigen Weichen, nicht an Einzelfehlern.** Wer die Lösung durch das
   Abarbeiten von Korrekturen an einem schwachen Entwurf verbessern will, erzeugt Flickwerk. Die
   Weichen werden deshalb vor dem Schreiben entschieden und dann durchgehalten.
2. **Ein falsches Zitat wiegt schwerer als ein fehlendes.** Belegt wird nur, was im Primärtext
   gelesen wurde, und jedes Argument gehört zu genau der Quelle, in der es steht.

## Arbeitsablauf

Arbeite die Phasen in dieser Reihenfolge ab. Details stehen in `references/arbeitsablauf.md`.

1. **Sachverhalt erschließen.** Den Sachverhalt vollständig lesen, Bearbeitervermerke wörtlich
   herausschreiben (welche Normen sind ausgeschlossen, welche Fragen sind gestellt, gibt es eine
   Umfangsvorgabe). Jede Sachverhaltsangabe ist ein Hinweis (Echo-Prinzip): Was der Sachverhalt
   erwähnt, soll im Gutachten wiederkehren, was er nicht anlegt, wird nicht geprüft.
2. **Recherche zu den offenen Rechtsfragen.** Unsichere Fragen erst recherchieren, dann entscheiden,
   nie aus dem Gedächtnis. Fundstellen mit Randnummer notieren und festhalten, ob der Volltext
   gelesen wurde.
3. **Weichen-Memo.** Für jede Weiche eine Entscheidung mit kurzer Begründung festhalten (Vorlage:
   `assets/weichen-memo.md`). Weichen, die eine Lehrperson oder Auftraggeberin vorgibt oder bei denen
   mehrere Lösungen vertretbar sind, mit dem Nutzer gemeinsam entscheiden. Danach gelten sie.
4. **Gliederung.** Vollständige nummerierte Gliederung mit allen Anspruchsgrundlagen, Einwendungen
   und Einreden, die der Sachverhalt anlegt, auch wenn sie im Ergebnis verneint werden. Breite ist
   erwünscht, Erfindungen nicht.
5. **Ausformulierung in einem Zug.** Ein Autor schreibt die Argumentation durchgehend auf Grundlage
   von Memo und Gliederung. Nicht abschnittsweise an verschiedene Agenten verteilen, sonst
   widersprechen sich die Teile.
6. **Belegliste.** Jede Fußnote mit Status erfassen: „im Volltext geprüft“ oder „vom Nutzer in einer
   Datenbank zu prüfen“ (Vorlage: `assets/belegliste.md`). Keine „[prüfen]“-Marker im Fließtext.
7. **Formale Prüfung.** `scripts/check_gutachten.py <datei.md>` ausführen und die Hinweise
   abarbeiten (siehe unten).
8. **Eine Korrektor-Lektüre.** Genau eine abschließende inhaltliche Lektüre, deren Befunde selbst am
   Volltext nachgeprüft und dann gesammelt eingearbeitet werden. Keine endlosen Prüfschleifen:
   „Zu viel Validierung“ macht den Text unstimmiger, nicht besser.

## Gutachtenstil

Die vollständigen Regeln mit Beispielen stehen in `references/stil.md`. Der Kern:

Jeder Prüfungspunkt folgt dem Vierschritt aus Obersatz, Definition oder Maßstab, Subsumtion und
Ergebnis. Der Obersatz steht im Konjunktiv und nennt den Anlass der Prüfung. Das Ergebnis steht erst
am Ende als Resultat der Argumentation, typischerweise mit „somit“ oder „folglich“. Auch
unproblematische Punkte werden als kurzes Gutachten geschrieben, nicht im Urteilsstil
(„X scheidet aus, weil …“ ist Urteilsstil).

Das Gutachten besteht ausschließlich aus Fließtext. Es enthält keine Stichpunktlisten, keine fett
gesetzten Einleitungsetiketten wie „**Grundsatz.** Text …“ und keine Überschrift, die in den Text
läuft. Jede Überschrift steht in einer eigenen Zeile und trägt eine Nummer nach dem Schema
Teil/Frage → A. → I. → 1. → a) → aa) → (1). Strukturbedarf wird über Gliederungsebenen gelöst,
nicht über Listen.

## Zitierweise

BGB-Normen werden ohne Gesetzesangabe zitiert, Absätze römisch, Sätze arabisch: „§ 123 II 1“ statt
„§ 123 Abs. 2 S. 1 BGB“. Andere Gesetze tragen ihre Bezeichnung, etwa „§ 377 I HGB“ oder
„Art. 229 § 71 I 1 EGBGB“. Normen stehen nicht in Klammern, sondern werden mit „gem.“, „iSv“ oder
„iVm“ in den Satz eingebaut. Die Zitierweise ist eine Hausregel, die sich an Vorgaben des Lehrstuhls
anpassen lässt (siehe `references/stil.md`, Abschnitt Anpassung).

## Fußnoten und Belege

Fußnoten stehen an der Definition oder dem Maßstabssatz, fast nie an Subsumtions- oder
Ergebnissätzen. Fehlt ein Maßstabssatz, wird er formuliert und die Fußnote dorthin gesetzt. Bei
Ansichten im Meinungsstreit trägt jede Ansicht ihren Beleg.

Keine bloßen Autoritätsverweise wie „So hat auch der BGH entschieden.“ Stattdessen die Begründung
des Gerichts als eigenes Sachargument formulieren und in der Fußnote belegen. Gerichtsnamen gehören
in die Fußnote, nicht in den Fließtext.

Die Belegregeln im Einzelnen (`references/belege.md`):

1. Nur zitieren, was im Primärtext gesehen wurde, oder es ausdrücklich auf die Prüfliste des Nutzers
   setzen.
2. Jedes Argument der Quelle zuordnen, in der es tatsächlich steht. Bei Instanzenzügen besonders
   aufpassen: Ein Argument des Berufungsgerichts ist kein Argument des Revisionsgerichts.
3. Randnummern am Volltext mit amtlicher Zählung prüfen. Zeitschriftenabdrucke lassen Randnummern
   teils weg oder zählen anders.
4. Den Entscheidungsgegenstand prüfen: Eine Entscheidung zu einer gewerberechtlichen Frage belegt
   nicht die zivilrechtliche Einordnung, eine Aussage „zum Nachteil des X“ nicht den allgemeinen
   Satz.
5. Anhängige Verfahren und Rechtsänderungen mit Stand-Vermerk in der Fußnote kennzeichnen.

## Umfang und Kürzungen

Kürzungen nie eigenmächtig vornehmen. Kürzungsvorschläge als nummerierte Liste mit der jeweils
eingesparten Zeichenzahl und der Gesamtsumme vorlegen und erst nach Freigabe umsetzen. Die
Zeichenzahl liefert `scripts/check_gutachten.py` (Text ohne Überschriften und Fußnoten).

## Formale Prüfung mit dem Skript

```bash
python3 scripts/check_gutachten.py pfad/zum/gutachten.md [weitere.md ...]
```

Das Skript meldet Überschriften ohne Nummer, Listenmarker, Fettetiketten, „Abs.“ und „BGB“ in der
Zitierweise, Normen in Klammern, typische Urteilsstil-Formulierungen, Gerichtsnamen und Semikolons im
Fließtext, Fußnoten an Ergebnissätzen sowie fehlende oder falsch nummerierte Fußnoten und zählt die
Zeichen. Die Hinweise sind Heuristiken: Jeden Treffer im Kontext beurteilen, nicht blind umformulieren.

## Zusammenarbeit mit dem Nutzer

Auf Deutsch antworten. Berichte knapp halten: was geändert wurde, was offen ist, Umfang in Zeichen.
In Antworten an den Nutzer sind Stichpunkte in Ordnung, im Gutachten nicht. Nur die Dateien ändern,
die der Auftrag nennt, und frühere Fassungen nicht überschreiben, sondern neue Fassungen in eigenen
Dateien oder Ordnern anlegen. Unsicherheiten offen benennen statt sie zu überspielen.
