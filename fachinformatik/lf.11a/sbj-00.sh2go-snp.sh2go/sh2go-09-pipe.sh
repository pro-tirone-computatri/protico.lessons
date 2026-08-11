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

EXC=sh2go-09
echo "executing Uebung $EXC"

# (1) Schreiben Sie das heutige Datum mit dem Format +'%Y%m%d" in eine Datei. Nutzen Sie dafür das Tool <date> 
# (2) Hängen Sie aus dem Skript heraus die Zeile '2024 war besser' an Ihre Datei
# (3) Lassen Sie die Datei mit cat einlesen.
# (4) Pipen Sie den eingelesen Inhalt als Input für grep.
# (5) Lassen Sie grep die 'war-besser'-Zeile herausfiltern.

# Hintergrund: 
#
# (A) Eine Pipe (Symbol '|') nimmt den Output des vorgehenden Tools und reicht in als Input an das nachfolgende Tool weiter.
# (B) cat nimmt einem Dateiname und liest den Inhalt der Datei ein und gibt ihn zeilenweis aus.
# (C) grep liest nicht nur aus einer Datei, sondern kann auch von stdin zeilenweise einlesen. 
# (D) die Pipe verknüpft hier die beiden Befehle <cat> und <grep>