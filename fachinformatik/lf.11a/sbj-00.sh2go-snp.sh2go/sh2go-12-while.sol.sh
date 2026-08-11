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

EXC=sh2go-12
echo "executing Uebung $EXC"

# (1) Lassen Sie aus dem Skript heraus eine Datei mit den 5 Zeilen
#  "Zeile 1" , "Zeile 2" , "Zeile 3" , "Zeile 4", "Zeile 5" befüllen
# (2) Lesen Sie die Datei mit <cat> zeilenweise ein.
# (3) Pipen Sie das an das Kommando <while>
# (4) Hängen Sie an je Zeile Ihr Kürzel an und lassen sie die ausgeben.

# Hintergrund: 
#
# (A) echo, >, >>, cat und  | wie gehabt.
# (B) <while> nimmt ein Kommando, führt es (solang es kann) aus,
#     speichert für jede Zeile das Ergebnis in einer Laufvariable 
# (C) mit do und done umgrenzt man dann ein Sektion von Befehlen,
#     in der man die Laufvariable nutzen kann.
#
# Beispiel cat datei | while read zeile; do echo zeile; done

echo "Zeile 1" > t.txt
echo "Zeile 2" >> t.txt
echo "Zeile 3" >> t.txt
echo "Zeile 4" >> t.txt
echo "Zeile 5" >> t.txt

cat t.txt |
while read l; 
  do echo "$l : krx"; 
done

P=`echo 1 2 3 4`

for i in $P; do echo $i; done
