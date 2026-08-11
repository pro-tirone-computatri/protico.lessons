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

EXC=sh2go-11
echo "executing Uebung $EXC"

# (1) Definieren Sie zwei Stringvariablen STRa und STRb mit den Inhalten "10" und "15"
# (2) Definieren Sie zwei Zahlvariablen NUMa und NUMb mit den Inhalten 10 und 15
# (3) Testen Sie STRa und STRb auf Stringgleichheit und geben Sie das Ergebnis als if-else-Statement aus.
# (4) Testen Sie NUMa und NUMb auf Zahlengleichheit und geben Sie das Ergebnis als if-else-Statement aus.
# (5) Testen Sie NUMa und NUMb auf Größenunterschied und geben Sie das Ergebnis als if-else-Statement aus.


# Hintergrund: 
#
# (A) Die bash kennt ein IF-Statement der Form 'if TEST-CMD; then TRUE-CMD; else FALSE-CMD;
# (B) TEST-CMD ist ein String der Form '[ STR1 = STR2 ]' oder '[ NUM1 -eq NUM2 ]' oder '[ NUM1 -lt NUM2 ]'
# (C.1) Sollen Variablen im Test als Strings vergleichen werden, muss = verwendet werden.
# (C.2) Sollen Variablen im Test als Zahlen vergleichen werden, muss -eq oder -lt verwendet werden. 
#       -eq :- equal  -lt :- less than 
# (D) TRUE-CMD und FALSE-CMD können jedes Shell-Kommando sein.
# (E) Wichtig: TEST-CMD, TRUE-CMD und FALSE-CMD müssen mit einem ; abgeschlossen werden.
# 
# Ergänzung: Bei den Tests ist das TEST-CMD - z.B. '[ STR = STR ]' - eine Abkürzung
# für den Aufruf `test STR = STR` des externen Tools <test>

# Disclaimer: Die ist nur ein äußerst kleiner Teil der Testmöglichkeiten.

STRa="10"
STRb="15"

NUMa=10
NUMb=15

if [ $STa = $STRb ]; then echo "equal string"; else  echo "different string"; fi

if [ $NUMa -eq $NUMb ]; then echo "equal number $NUMb"; else  echo "different numbers $NUMa : $NUMb"; fi

if [ $NUMa -lt $NUMb ]; then echo "$NUMa < $NUMb"; else  echo "$NUMa >= $NUMb"; fi
