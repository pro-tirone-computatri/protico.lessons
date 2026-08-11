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

EXC=sh2go-06
echo "executing Uebung $EXC"

# (1) Lassen Sie Ihr Skript in eine Datei 'heute.txt' das Wort 'morgen' schreiben
# (2) Weisen Sie den Inhalt der Datei 'heute.txt' mit cat und backticks der Variable GESTERN zu. 
# (3) Benennen Sie die Datei 'heute.txt' aus dem Skript heraus in 'gestern.txt' um.
# (4) Lassen Sie Ihr Skript den Inhalt der Vartiable GESTERN in eine Datei 'morgen.txt' schreiben.
# In welcher Datei steht 'gestern'?


# Hintergrund: 
#
# (A) zu <cat>, backticks und umlenken siehe Übung 1, 4 und 5
# (B) Etwas aus einem Skript heraus in eine Datei zu schreiben, geschieht über das Umlenken des Outputs
# (C) Eine Dateinamen zu ändern = die Datei umzubennnen, geschieht über das Kommando move = <mv>:
#     Es nimmt den alten und den neuen Dateiname als Parameter und führt den Befehl aus.

