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

EXC=sh2go-19
echo "executing Uebung $EXC"

# Definieren Sie eine Funktion, die 2 Zahlen nimmt, 
# sie addiert und die Summanden und Summe ausgibt. 
# Rufen Sie Ihre Funktion für die Zahlenpaare 2,3 und 5,6 auf


# Hintergrund: 
#
# (a) Eine Funktion wird definiert mit dem Konstrukt
#     myf() { 
#       ...
#     }
# (b) Anstelle der Punkte können beliebig viele Bash-Kommandos eingesetzt werden.
# (c) In einer Funktion können Variablen definiert werden.
#     myf() { 
#       global EXTVAR # macht eine externe Variable intern bekannt 
#       local LOCVAR # definiert eine Variable im lokalen Kontext neu
#     }
# (d) Einer Funktion können Argumente mitgegeben werden.
#     Sie werden mit $1 - $n abgerufen.
#     $0 steht nicht für den Funktionsnamen, sondern wieder für den Skriptnamen
#
# Hinweis:
#
# Sollen die Skript(!)parameter $1 - $n in ider Funktion erreichbar sein,
# können sie entweder explizit an die Funktion übergeben werden
# oder außerhalb gesondert definiert und in der Funktion als global
# bekanntgemacht werden.

