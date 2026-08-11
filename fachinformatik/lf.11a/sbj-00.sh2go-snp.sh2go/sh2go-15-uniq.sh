#!/bin/sh
#
# This file is part of the Open Source project 'proTirone'
# (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
# It is distributed under the terms of the creative commons license
# CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
#

# Lesehinweis: 
# In spitzen Klammern schreibe ich stets Tools und ihre Parameter.
# Die Tools stellt Ihnen Betriebssystem zur Verfügung.
#
# Beispiel: 
# Rufen Sie <echo dies> auf, meint, dass Sie an der
# Kommandozeile echo dies eingeben. Wo sich das Tool, hier
# <echo> bei Ihnen befindet, können Sie mit <which echo> erfragen

EXC=sh2go-14
echo "executing Uebung $EXC"

# Schreiben Sie ein Skript, dass zuerst die folgende Zeilen in eine Datei schreibt.
# eins
# eins
# zwei
# drei
# zwei
# eins
#
# Lassen Sie Ihr Skript dann diese erzeugte Datei einlesen, löschen Sie alle Duplikate
# und geben sie das Ergebnis nach stdout aus.


# Hintergrund: 
#
# Das Tool <uniq> löscht in einer Datei oder in einer über stdin zeilenweise eingelesenen
# Datei doppelte auftretende Zeile (Duplikate). Allerdings erwartet es dafür eine
# sortierte Liste. Sonst findet es nicht alle Doubletten.
#


