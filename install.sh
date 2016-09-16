#!/bin/sh

source=`pwd`
templates=~/.pandoc/templates
latex=`kpsexpand '$TEXMFHOME/tex/latex/dwp'`
bin=/usr/local/bin
if [ "$1" = "-y" ]
then
  iarg=""
else
  iarg="-i"
fi

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
  install='ln -s -v -f'
else
  install='cp -r -p -v'
fi


mkdir -p "$templates"
$install $iarg "$source/DWP.latex" "$source"/*.csl "$templates/"
mkdir -p "$latex"
$install $iarg "$source"/img/* "$latex/"
sudo $install $iarg "$source/dwp.py" "$bin/dwp"
