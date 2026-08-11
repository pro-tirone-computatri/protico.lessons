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

EXC=sh2go-02
echo "executing Uebung $EXC"

# (0.A) Definieren Sie eine Variable MORNING
# (0.B) Weisen Sie der Variable MORNING den Wert 'evening' zu
# (0.C) Definieren Sie eine Variable EVENING
# (0.D) Weisen Sie der Variable EVENING den Wert 'morning' zu
# (1) Definieren Sie eine Variable OUTPUT 
# (2) Weisen dieser Variable den Wert "Good ${MORNING}" zu. 
# (3) Lassen Sie echo diese Variable ausgeben, und zwar
#     - erst direkt
#     - dann zur Expansion eingebettet in einen String der Form ""
#     - dann zur Expansion eingebettet in einen String der Form ''
# Worin unterscheidet sich das Ergebnis?
#
# (4) Überschreiben sie die Variable OUTPUT mit dem String "Good ${EVENING}" 
# (5) Wiederholen sie (3).
# Worin unterscheidet sich das Ergebnis? Was passiert da?
#
#
# Hintergrund: 
#
# (A) Variablen können an jeder Stelle eines Skriptes definiert und mit einem Wert belegt werden.
#     Sie werden zumeist in Großbuchstaben mit Unterstrichen erfasst:
# (B) Jeder Variable wird mit einem '=' ihr (nächster) Wert zugewiesen
# (C) Jede Variable kann an jeder Stelle 'überschrieben' [mit einem neuen Wert beglegt] werden
# (D) Den Wert einer Variable ruft man ab, indem man ihr dort, wo man den braucht, ein $ voransetzt.
# (E) Variablen können in Strings eingebaut werden. Geht ihnen ein $ voraus, wird der aktuelle Wert
#     in den String eingefügt. Das nennt man Variablen- bzw. Parameterexpansion.
# (F) Gelegentlich ist es übersichertlicher, die Variable in geschweifte Klammern zu fassen,
#     und Konstrukt das $-Zeichen voranzusetzen.

MORNING="evening"
EVENING="morning"
OUTPUT="Good ${MORNING}"

echo $OUTPUT
echo "$OUTPUT"
echo '$OUTPUT'

OUTPUT="Good ${EVENING}"

echo $OUTPUT
echo "$OUTPUT"
echo '$OUTPUT'




