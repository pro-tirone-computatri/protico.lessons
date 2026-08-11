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

EXC=sh2go-20
echo "executing Uebung $EXC"

# Geben Sie einen dreizeiligen Text mit den Zeilen L1, L2 L3
# mit einem einzigen Echo-Befehl aus. Demonstrieren Sie
# die 3 Varianten
# (1) Ausgaben eines einzeiligen Strings mit einbettetem \n
# (2) Ausgabe eines Heredocs mit cat
# (3) Einlesen eines Heredocs in eine Variable mit read
#     und Ausgabe der Variable mit <echo>^
#
# Hintergrund: 
#
# (a) In einen String können Zeilenumbruchsymbole (\n) eingebetten werden
#     Im Code steht ein einzeiliger String, ausgegeben wird ein mehrzeiliger Text,
#     sofern echo mit der Option -e aufgerugfen wird.
#
# (b) Alternativ kann ein Heredoc definiert und an einen Befehl übergeben werden:
#
#     cat << MyEndOfFile
#     Zeile
#     für
#     Zeile
#     MyEndOfFile
#
#     Der Begrenzer 'MyEndOfFile' wird vom Programmierer gewählt
#     und dem Heredoc voran- und hintangestellt
#
# (c) Statt das Heredoc direkt an ein Tool zu übergeben, kann es
#     auch per read in eine Variable eingelesen werden:
#
#     read -r -d '' MyVar << EOM
#     Zeile
#     für
#     Zeile
#     EOM
#
#     und diese dann mit echo ausgegeben werden:
#
#     echo "$MyVar"
#     
#     Hinweis: Ohne umgrenzende Anführungszeichen werden die Zeilenumbrüche ignoriert


echo -e "L1\nL2\nL3\n"

cat << EndOfMessage
L1
L2
L3

EndOfMessage

read -r -d '' MV << EndOfMessage
l1
l2
l3

EndOfMessage

echo $MV
echo "versus"
echo "$MV"
