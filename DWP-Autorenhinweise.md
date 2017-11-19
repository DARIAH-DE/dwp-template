---
title: DARIAH Working Paper Workflow
subtitle: Hinweise für Autorinnen und Autoren
author: 
- Thorsten Vitt
- Mirjam Blümm
lang: de
date: 2016
abstract: |
    Für die Publikation der DARIAH-Working-Papers gibt es einen Workflow
    auf der Basis von Markdown, das mit Pandoc und LuaLatex formatiert wird.

    Dieser Artikel beschreibt einige Spezifika der
    Working-Paper-Vorlage; Details zur Markdown-Syntax findet man z. B. auf der
    Pandoc-Homepage.
wpno: 0
...

# Artikel schreiben

Die Texte sollen mit Markdown ausgezeichnet werden. Zum Übersetzen wird Pandoc verwendet, es sind entsprechend also Konstrukte aus [Pandoc's Markdown](http://pandoc.org/MANUAL.html#pandocs-markdown) möglich. 

Diese Datei stellt lediglich die wichtigsten Konstrukte sowie einige Besonderheiten der _DARIAH Working Papers_ zusammen, für eine umfassende Dokumentation sei auf die o.g. Pandoc-Dokumentation verwiesen.

Es wird nicht von den AutorInnen erwartet, ein _camera-ready PDF_ abzuliefern. Wer die Umgebung zum Erzeugen der Artikel aufsetzen mag, findet im [Text zur Redaktionsumgebung](https://github.com/DARIAH-DE/dwp-template/blob/master/DWP-Redaktionsumgebung.pdf) Hinweise.

# Text

Markdown-Dateien sind einfache Textdateien so wie diese. Zeilenumbrüche werden wie Leerzeichen behandelt, für einen Absatzwechsel schreibt man eine Leerzeile in den Text.

_Kursivierungen_ werden erzeugt, indem man die zu kursivierenden Passagen `_mit Unterstrichen_` (oder alternativ Sternchen) umschließt. Für __Fettdruck__ verwendet man `__doppelte Unterstriche__` oder doppelte Sternchen. Überschriften sind Absätze, die (je nach Ebene) mit einem bis drei Rautenzeichen `#` beginnen, gefolgt von einem Leerzeichen:

```markdown
## Überschrift zweiter Ebene
```

## Listen

Um eine Liste zu erzeugen, beginnt man eine Zeile mit einem Aufzählungszeichen: `*`, `-` oder `+`, gefolgt von einem Leerzeichen. Das Aufzählungszeihen darf bis zu drei Leerzeichen eingerückt sein. Einzelne Leerzeilen zwischen den Listeneinträgen sind erlaubt.

Besteht ein Listeneintrag aus mehreren Absätzen, so sind Leerzeilen obligatorisch und man rücke die Folgeabsätze um vier Leerzeichen ein. Verschachtelte Listen werden ebenfalls um vier Leerzeichen eingerückt.

Nummerierte Listen folgen derselben Syntax:

```markdown
 1. Beispieleintrag
 2. Noch ein Eintrag.

    Im Gegensatz zum vorherigen besteht dieser Eintrag aus mehreren Absätzen.
    Man beachte die Einrückung.

 3. Hier nun eine untergeordnete Liste:

    * Eintrag,
    * noch ein Eintrag,
    * weiterer Eintrag.
```
erzeugt

 1. Beispieleintrag
 2. Noch ein Eintrag.

    Im Gegensatz zum vorherigen besteht dieser Eintrag aus mehreren Absätzen.
    Man beachte die Einrückung.

 3. Hier nun eine untergeordnete Liste:

    * Eintrag,
    * noch ein Eintrag,
    * weiterer Eintrag.

## Code und Blockformate

Um inmitten eines Absatzes ein Stück Code in `Festbreitenschrift` zu formatieren, umschließt man das enstprechende Stück Code mit Backticks:

```markdown
inmitten eines Absatzes ein Stück Code in `Festbreitenschrift` zu formatieren,
```

Ganze Codeblöcke können entweder um vier Leerzeichen eingerückt werden oder – diese Variante empfehlen wir – mit Zeilen aus je drei Backticks umgeben werden. Unmittelbar hinter der einleitenden Backtickreihe kann der Sprachenname angegeben werden, um Syntax-Highlighting zu erreichen:

    ```python
    def foo():
        return "bar"
    ```

```python
def foo():
    return "bar"
```

Soll für Gedichte o.ä. der Zeilenfall erhalten bleiben, aber ansonsten normaler Text formatiert werden, beginnt man die Zeilen mit `| `. Zeilen mit Blockzitaten wird `> ` vorangestellt.

## Formeln

Mathematische Formeln können in \LaTeX-Syntax eingegeben werden. Inline-Formeln wie in $x_i, i < n$ werden zwischen einfachen Dollarzeichen geschrieben: `$x_i, i < n$`, das sollte aus Konsistenzgründen auch bei der Erwähnung von Variablen wie $n$ im Text geschehen. Für abgesetzte Formeln verwendet man doppelte Dollarzeichen: $$\bar{x} = \frac{1}{n} \sum_{i=1}^n x_i$$

## Bilder

Bilder sollten als PDF-, PNG- oder JPEG-Datei mitgeliefert werden. Sie werden über eine Bildreferenz eingebunden, die in einem eigenen Absatz stehen sollte (Leerzeile davor und danach):

```
![Ein Beispielbild](img/Logo_Working-Papers.pdf)
```
![Ein Beispielbild](img/Logo_Working-Papers.pdf)

In den eckigen Klammern steht die Bildunterschrift, die durchaus Formatierungen enthalten kann.

Bitte beachten Sie, dass Groß- und Kleinschreibung in Bildreferenz und Dateinamen zueinander passen und verzichten Sie möglichst auf Leer- und Sonderzeichen in den Dateinamen.

Ohne weitere Angaben wird eine in den Bildmetadaten hinterlegte Druckgrößenangabe berücksichtigt, die Bildgröße jedoch auf die Größe des Textbereichs begrenzt. Da die entsprechenden Metadaten oft falsch sind, sollten sie bei Bildern in Seitengröße überprüft und ggf. korrigiert werden. Das geht z. B. mit [ImageMagick](http://www.imagemagick.org/script/command-line-options.php#density), das folgende Kommando setzt z.B. die Auflösung aller JPEG-Bilder auf 300 dpi:

```sh
mogrify -density 300 -units PixelsPerInch *.jpg
```

Bei Gimp heißt die entsprechend Option _Print Size_. Alternativ sind Größenangaben beim Einbinden des Bilds möglich:

![25% der Textbreite](img/Logo_Working-Papers.pdf){width=25%}

```![25% der Textbreite](img/Logo_Working-Papers.pdf){width=25%}
```

Die Bilder werden über eine Heuristik an der Stelle der Einbindung, oben oder unten auf der aktuellen Seite oder einer der folgenden Seite, oder auf einer separaten, nur für Abbildungen vorgesehenen Seiten platziert. Falls alle Abbildungen am Ende des Dokuments in einem Anhang platziert werden sollen, so kann das Kommando `\floatappendix` benutzt werden, um die Platzierungseigenschaften entsprechend anzupassen:

```markdown
\floatappendix

## Abbildungen

![Eines der ziemlich großen Bilder](img/some-image.pdf)
```

## Links und Fußnoten

Verweise auf [Webseiten](https://de.dariah.eu/working-papers) bestehen i.d.R. aus einem Linktext in eckigen gefolgt von der vollständigen URL (mit http://!) in runden Klammern: `[Webseiten](https://de.dariah.eu/working-papers)`. Im Text wird der Linktext anklickbar, die URL kommt zusätzlich in eine Fußnote. Soll eine URL – wie <http://de.dariah.eu/> – im Text auftauchen, so setze man sie in spitze Klammern: `<http://de.dariah.eu/>`, sie wird dann zum Link, erzeugt jedoch keine Fußnote.

Sonstige Fußnoten können wie im Beispiel inline^[dann aber ohne Absätze] oder separat[^bsp] gesetzt werden.

[^bsp]: Separate Fußnoten können durchaus auch aus mehreren Absätzen bestehen.
    
    Es gilt die übliche vier-Leerzeichen-Einrückregel.

```markdown
Sonstige Fußnoten können wie im Beispiel inline^[dann aber ohne Absätze] 
oder separat[^bsp] gesetzt werden.

[^bsp]: Separate Fußnoten können durchaus auch aus mehreren Absätzen bestehen.
    
    Es gilt die übliche vier-Leerzeichen-Einrückregel.
```
Bei separaten Fußnoten kann das Fußnotenkürzel (hier `bsp`) beliebig gewählt werden, die Fußnote kann an einer beliebigen Stelle (in eigenem Absatz) gesetzt werden. Achtung: In Fußnoten sollten URLs nur in der `<>`-Form gesetzt werden, da Fußnoten in Fußnoten nicht unterstützt werden.

# Bibliographie

Für die Bibliographie empfehlen wir, die Literaturverzeichnis-Einträge __im BibLaTeX- oder BibTeX-Format__ in einer Datei mit gleichem Namen wie der Artikel und der Endung `.bib` zu verwalten und sich für die Zitationen an die entsprechenden [Pandoc-Konventionen](http://pandoc.org/MANUAL.html#citations) zu halten – in diesem Fall wird das Literaturverzeichnis automatisch einheitlich und entsprechend der Stilvorlagen formatiert. AutorInnen, die Ihre Literaturangaben in einem Freitextformat vorliegen haben, können z. B. einen Dienst wie [AnyStyle](https://anystyle.io) in Anspruch nehmen, um daraus eine BibTeX-Datei zu erzeugen. Das Literaturverzeichnis in Textform anzuliefern ist ebenfalls möglich, AutorInnen sind dann jedoch für Formatierung entsprechend der Richtlinien, Konsistenz und Sortierung selbst verantwortlich. 

Wird ein solches automatisches Literaturverzeichnis verwendet, so muss der Artikel mit diesem Kommando enden:

```latex
\biblio
```

Das Kommando setzt automatisch die entsprechende Überschrift und passt die Formatierungsvorgaben an.

Literaturverweise können dann jeweils unter Verwendung des Literaturverweisschlüssels aus der .bib-Datei z.B. auf die folgenden Weisen gesetzt werden:

* Im einfachsten Fall schreibt man `[@hh2010]` und erzeugt [@hh2010]. 
* Präfixe und Seitenverweise sind möglich wie in `[vgl. @hh2010, S. 1]` [vgl. @hh2010, S. 1].
* Textverweise ohne Klammern um den Autoren wie in @hh2010a werden ohne die eckigen Klammern geschrieben: `@hh2010a`
* Mehrere Verweise teilen die eckigen Klammern: `[vgl. etwa @hh2010; @hh2010a; @hh2010b]` [vgl. etwa @hh2010; @hh2010a; @hh2010b]
* Mit `-` kann man den Autor unterdrücken: "Wie Hagen [-@hh2010] schreibt, …" `Wie Hagen [-@hh2010] schreibt,`



# Titeldaten

Titeldaten und einige Einstellungen gehören in einen Metadatenblock im YAML-Format. Der Block beginnt mit einer Zeile aus drei Bindestrichen `---` und endet mit einer Zeile aus drei Punkten `...`. Metadatenfelder beginnen mit dem Feldnamen am Anfang der Zeile, dann folgt ein Doppelpunkt und ein Leerzeichen und schließlich der Inhalt des Felds.

Einige Felder (z. B. die Autorenliste) kann mehrere Werte aufnehmen. Dazu schreibt man eine YAML-Liste: Die Zeile mit dem Feldnamen endet nach dem Doppelpunkt, darauf folgt ein Listeneintrag pro Zeile, beginnend mit einem Bindestrich. Das Feld `abstract` kann mehrere Absätze umfassen, dazu endet die Zeile mit dem Schlüsselwort mit einem `|` und es folgen die Textabsätze eingerückt. Der Metadatenblock kann also z. B. so aussehen:

    ---
    title: DARIAH Working Paper Workflow
    subtitle: Spaß mit Pandoc
    author: 
    - Thorsten Vitt
    - Mirjam Blümm
    lang: de
    date: 2016
    abstract: |
        Für die Publikation der DARIAH-Working-Papers empfehlen wir einen Workflow
        auf der Basis von Markdown, das mit Pandoc und LuaLatex formatiert wird.

        Dieser Artikel beschreibt die Installation und einige Spezifika der
        Working-Paper-Vorlage; Details zur Markdown-Syntax findet man z. B. auf der
        Pandoc-Homepage.
    ...

Die folgenden Metadatenfelder stehen zur Verfügung:

| Feld                  | Bedeutung                                                     |
|-----------------------|---------------------------------------------------------------|
| title                 | Titel des Artikels.                                           |
| subtitle (optional)   | Untertitel.                                                   |
| lang                  | Sprache, in der der Artikel verfasst ist: `de` oder `en`.     |
| author                | Autor des Artikels. Bei mehreren Autoren Liste verwenden.     |
| longauthor (optional) | Autoren mit Fußnotenzeichen für Institute                     |
| institute             | Institut(e), ggf. mit Fußnotenzeichen (Liste möglich)         |
| date                  | Veröffentlichungsjahr                                         |
| abstract              | Zusammenfassung                                               |
| keywords-de           | Schlagwörter auf Deutsch (als Liste)                          |
| keywords-en           | Schlagwörter auf Englisch (als Liste)                         |
| wpno                  | DARIAH-Working-Papers Nr. (wird von der Redaktion eingesetzt) |
| urn                   | URN (wird von der Redaktion eingesetzt)                       |

Für Texte, die zuvor als DARIAH-Report veröffentlicht worden sind, sollen die folgenden Metadaten ergänzt werden:

| Feld                  | Bedeutung                                        |
|-----------------------|--------------------------------------------------|
| report-number         | Nummer des Reports, z. B. `1.2.3`                |
| report-date           | Veröffentlichungszeitraum, z. B. `Dezember 2015` |
| report-fkz (optional) | Förderkennzeichen                                |

Für weitere Anmerkungen, die in einem eigenen Matadatenfeld ergänzt werden sollen, stehen folgende Felder zur Verfügung:

| Feld                  | Bedeutung                                        |
|-----------------------|--------------------------------------------------|
| publish-note          | Zusätzliche Angaben (Freitext) z.B. für die Quellenangabe von Erstpublikationen, Konferenzbeiträge usw. |
| urn-alt (optional)    | URN der Erstveröffentlichung |

\biblio
