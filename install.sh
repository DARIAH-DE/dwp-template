#!/bin/sh

source=`pwd`
templates=~/.pandoc/templates
latex=`kpsexpand '$TEXMFHOME/tex/latex/dwp'`
bin=/usr/local/bin

cat <<EOF
DWP-Installation
----------------

Dieses Script installiert aus dem Ordner $source:

- Vorlage und Bibliographiestil nach $templates
- Bilder nach $latex
- Skript nach $bin

Sollen die Dateien verlinkt statt kopiert werden? Wenn Du 'j' antwortest,
darfst Du das Verzeichnis $source nicht löschen oder verschieben, aber dafür
musst Du nach einer Aktualisierung das Installationsscript nicht erneut laufen
lassen. [j/n]
EOF
read dolink
if [ "$dolink" = "j" ]
then
  install='ln -s -v -i'
else
  install='cp -r -p -v -i'
fi


mkdir -p "$templates"
$install "$source/DWP.latex" "$source"/*.csl "$templates/"
mkdir -p "$latex"
$install "$source"/img/* "$latex/"
sudo $install "$source/dwp.py" "$bin/"
