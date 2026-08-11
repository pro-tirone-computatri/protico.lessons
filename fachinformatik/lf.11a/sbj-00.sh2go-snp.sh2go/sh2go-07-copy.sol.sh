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

EXC=sh2go-07
echo "executing Uebung $EXC"

# (1) Lassen Sie Ihr Skript in eine Datei 'today.txt' das Datum von heute schreiben 
# (2) Kopieren Sie die Datei 'today.txt' unter dem Namen 'yesterday.txt' 
# (3) Weisen Sie das Datum aus der Datei 'today.txt' der Variable TODAY zu
# (4) Weisen Sie das Datum aus der Datei 'yesterday.txt' der Variable TOMORROW zu
# (5) Lassen Sie den Satz ausgeben "$TODAY is $TOMORROW"


# Hintergrund: 
#
# (A) Um eine Datei in eine neue hinein zu kopieren, nutz man das Kommando <cp>
# (B) Es nimmt den Namen (Pfad) zur Originaldatei und den Namen (Pfad) zur neuen Datei
#     und legt die neue Datei mit dem Inhalt der alten an

echo `date +'%Y-%m-%d'` > today.txt
cp today.txt yesterday.txt
TODAY=`cat today.txt`
TOMORROW=`cat yesterday.txt`

echo "$TODAY is $TOMORROW"


