---
title: DARIAH Working Paper Workflow
subtitle: Redaktionsumgebung – Work in Progress
author: 
- Thorsten Vitt
- Mirjam Blümm
lang: de
date: 2016
abstract: |
    Für die Publikation der DARIAH-Working-Papers gibt es einen Workflow
    auf der Basis von Markdown, das mit Pandoc und LuaLatex formatiert wird.

    Dieser Artikel beschreibt die Installation der Working-Paper-Vorlage und einige weitere Themen für Redakteure. Autoren finden Hinweise zur Formatierung des Texts in den [Autorenhinweisen](https://github.com/DARIAH-DE/dwp-template/blob/master/DWP-Autorenhinweise.pdf).
wpno: 0
...


# Voraussetzungen

* Pandoc
* LaTeX-Installation mit LuaLaTeX, z.B. aktuelles TeX-Live
* pandoc-citeproc (für das Literaturverzeichnis-Processing)
* Python 3 (für das Convenience-Skript)

# Installation

(Es gibt ein einfaches, experimentelles Installationsscript `install.sh`, das auf Linux und MacOS X funktionieren sollte.)

Die Schriften [WeblySleek UI](http://www.dafont.com/weblysleek-ui.font) und [Iosevka in der Default-Variante (Download `01-*`)](https://be5invis.github.io/Iosevka/)
entsprechend dem Betriebssystem installieren. Für übliche Linux-Distributionen ist es ausreichend, die TTF-Dateien in den Ordner `~/.fonts` zu legen.



Einige Dateien aus diesem Verzeichnis müssen über das Dateisystem verteilt werden. Ich empfehle, die entsprechenden Dateien per symbolischem Link zu verlinken statt sie zu kopieren, um für Aktualisierungen gerüstet zu sein:

* __DWP.latex__ ist das Pandoc-Template, es muss in das Verzeichnis `~/.pandoc/templates`.
* Die __`*.csl`-Dateien__ sind die Styles für die Literaturverwaltung, sie stammen aus dem [Zotero Style Repository](https://www.zotero.org/styles?q=chicago&format=author-date). `dwp.py` sucht diese Styles ebenfalls im Verzeichnis `~/.pandoc/templates`
* Die Bilder aus dem `img`-Ordner werden für die Titelseite benötigt. Sie werden in einem LaTeX-Baum gesucht.
* `dwp.py` ist ein Script zum einfachen Aufrufen von Pandoc mit entsprechenden Parametern. Es sollte irgendwo in den `$PATH`.

Unter der Annahme, dass dieses Verzeichnis unter `~/projects/dwp-template` liegt:

```bash
mkdir -p ~/.pandoc/templates
cd ~/.pandoc/templates
ln -s ~/projects/dwp-template .
mkdir -p `kpsexpand '$TEXMFHOME/tex/latex'`
cd `kpsexpand '$TEXMFHOME/tex/latex'`
ln -s ~/projects/dwp-template .
cd /usr/local/bin
sudo ln -s ~/projects/dwp-template .
```

Nach erfolgreicher Installation sollte es in jedem Verzeichnis möglich sein, mit `dwp datei.md` die entsprechende Datei in PDF zu übersetzen.

# Benutzung

Das beigefügte Skript `dwp.py` kann einfach mit `dwp artikeldatei.md` aufgerufen werden. Es ruft Pandoc mit den richtigen Parametern auf, um `artikeldatei.pdf` zu erzeugen. Das kann dann z. B. so aussehen:

```bash
pandoc -o article.pdf --latex-engine=lualatex --template=DWP \
       --filter=pandoc-citeproc --bibliography=article.bib \
       --csl=$HOME/.pandoc/templates/chicago-author-date.csl \
       --metadata=link-citations:true \
       article.md
```

`dwp` kann auch mit weiteren Pandoc-Parametern aufgerufen werden, es reicht alle Parameter an Pandoc weiter und lässt dafür ggf. die selbst generierten Versionen weg.

# Troubleshooting

## irgendwas mit UTF-8

Eingabedatei ist nicht UTF-8-codiert. Im Texteditor öffnen und als UTF-8 speichern.

## PDF-Datei kann nicht erzeugt werden, keine ordentliche Fehlermeldung

1. TeX-Datei erzeugen lassen – das geht entweder auf die entsprechende Rückfrage oder mit `dwp -o article.tex article.md`
2. TeX-Datei manuell mit LuaLaTeX übersetzen lassen: `lualatex article.tex`, Fehlermeldungen prüfen

## Fehlermeldung wegen `\bibname`

Metadatenfeld `lang: de` oder `lang: en` angeben!

## `.bib` vorhanden und kein Literaturverzeichnis

Heißt die `.bib` so wie die `.md`? 

Wird auch wirklich zitiert, dh mit `@mueller2012` (entsprechend den Keys im `.bib`)? Siehe `DWP-Autorenhinweise.md` und `DWP-Autorenhinweise.bib`: Im `.md` muss `@Eijkhout1991` oder `[@Eijkhout1991]` stehen, um den u.a. Eintrag zu zitieren:

```bibtex
@BOOK{Eijkhout1991,
  title = {\TeX\ by Topic. A \TeX nician's Reference},
  publisher = {Addison-Wesley},
  year = {1991},
  author = {Victor Eijkhout},
  address = {London},
  keywords = {general},
}
```

Literatur, die nicht in Pandoc-Syntax zitiert wird, landet auch nicht im Literaturverzeichnis.

Wenn Autoren `.bib` anliefern, aber _nicht_ korrekt zitieren, kann man sich behelfen, indem man exakt folgenden Metadateneintrag zum YAML-Header hinzufügt:

```yaml
nocite: '@*'
```
In diesem Fall werden alle Einträge der `.bib`-Datei im Literaturverzeichnis gesetzt, auch solche, die nicht zitiert werden. Convenience-Features wie einheitliche Zitationskeys und Links von der Jahreszahl ins Literaturverzeichnis gehen damit natürlich nicht.


# Umgang mit Dateien in Office-Formaten

Wenn Dateien in Office-Formaten angeliefert werden empfiehlt sich folgender Workflow:

1. OpenOffice-Dateien nach DOCX konvertieren, die Pandoc-Unterstützung von DOCX ist besser
2. `pandoc -o article.md --extract-media=article_assets article.docx`. Erzeugt aus der Worddatei eine Markdown-Datei namens `article.md`, extrahiert die Bilder und speichert sie im Verzeichnis `article_assets` (wird ggf. angelegt)
3. Markdown-Datei nachbearbeiten

Vorteil: Bilder werden gleich ausgepackt, Grundformatierungen bleiben erhalten
