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

EXC=sh2go-18
echo "executing Uebung $EXC"

# Definieren Sie eine Arrayvariable, die die Zahlen 0 - F enthält.
# Geben Sie die Anzahl der Arraywerte aus.
# Iterieren Sie dann in 2 Schleifen über das Array und geben Sie
# in einer Zeile alle Hex-Werte aus, die ein Byte annehmen kann.


# Hintergrund: 
#
# (1) In der Bash kann man eine Arrayvariable über den Index definieren:
#     Beispiel:
#       HEXARR[0]=0
#       HEXARR[9]=A 
#       HEXARR[10]=B 
#     definiert ein Array mit 3 Werten .
# (2) Die Größe des Arrays erhält man mit dem Befehl
#       echo ${#HEXARR[*]}
# (3) Außerdem kann man ein Array auch auf einen Schlag befüllen:
#       HEXARR=(0 a b)
#       Dann werden die Arrayzellen aber automatisch durchnumeriert.
# (4) Ein Array als Ganzes ausgeben, kann man mit den Befehlen
#       <echo ${HEZARR[*]}> oder <echo ${HEZARR[@]}>
# (5) Auf einen den Wert einer Arrayzelle greift man zu mit dem Befehl
#       ${HEYARR[2]}
# (5) Will man aus den Arraywerten neue generieren, muss man über das 
#     Array iterieren. Dazu nutzt man die for-Schleife 
#       <for i in {0..3}; do echo ${HEXARR[$i]}
#
# Erinnerung: Ohne komplexere Konstruktion verträgt die Konstruktion {0..18}  
# in der for-Schleife keine Variablen. Am Enfachsten gibt man den Range literal an.

HEXARR=(0 1 2 3 4 5 6 7 8 9 a b c d e f)

echo ${#HEXARR[*]}

for ih in {0..15}; do 
  for il in {0..15}; do 
    echo -n "0x${HEXARR[$ih]}${HEXARR[$il]} ";
  done;
done



