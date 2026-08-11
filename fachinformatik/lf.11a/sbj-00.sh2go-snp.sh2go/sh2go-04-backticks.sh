#!/bin/sh
#
# This file is part of the Open Source project 'proTirone'
# (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
# It is distributed under the terms of the creative commons license
# CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
#

# Lesehinweis
# In spitzen Klammern schreibe ich stets Tools und ihre Parameter.
# Die Tools stellt Ihnen Betriebssystem zur Verfügung.
#
# Beispiel: 
# Rufen Sie <echo dies> auf, meint, dass Sie an der
# Kommandozeile echo dies eingeben. Wo sich das Tool, hier
# <echo> bei Ihnen befindet, können Sie mit <which echo> erfragen

EXC=sh2go-04
echo "executing Uebung $EXC"

# (1) Weisen Sie einer Variable den Output des Kommandos <echo HOHOHO> zu
# (2) Geben Sie den Wert Ihrer Variable mit echo aus.

# Hintergrund: 
#
# (A) Alle Tools erzeugen einen Output-String bzw. Text.
# (B) Den Output eines Tools kann man im Skript auffangen, indem man es
#     nach Variable und Gleichheitszeichen mit Backticks aufruft:
#     VAR=`tool test`

