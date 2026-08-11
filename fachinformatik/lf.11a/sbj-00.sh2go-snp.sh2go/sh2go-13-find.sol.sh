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

EXC=sh2go-13
echo "executing Uebung $EXC"

# (1) Erstellen Sie ein Script, das eine Liste aller Dateinamen von sh2go-Aufgaben in einer 
#     Datei zusammenstellt und dabei die Dateinamen der Aufgaben mit Lösungen ignoriert.
#
#
# Hintergrund: 
#
# (A) <ls *.*> listet alle Dateien und Ordner im aktuellen Pfad auf, die einen Punkt im Dateinamen haben.
#     Mit Änderung des Parameters '*.*' in 'sh2go*' oder '*.sh' würden in diesem Fall alle Skripte aufgelistet.
#     Gleichwohl würden immer noch die Aufgaben und die Lösung erscheinen. Die Frage zielt aber auf die Aufgaben
# (B) <find . -type f> findet vom aktuellen Pfad '.' aus alle Dateien und listet sie auf. 
#
# Mit beiden Funktionen kann man
# * die Liste der gefundenen Dateien (Einträge) in ein zweites Tool zur Verarbeitung pipen:
#   * <find . -type f -name "*.sh" | while read l; do echo $l; done> oder
#   * <ls *.sh | while read l; do echo $l; done>
# * die Liste der gefundenen Dateien (Einträge) in eine Textdatei umlenken:
#   * <find . -type f -name "*.sh" > list-of-sh2go-tasks.txt>
#   * <ls  *.sh > list-of-sh2go-tasks.txt>

find . -name "*.sh"  ! -name "*sol.sh" > list-of-sh2go-tasks.txt

find . -name "*.sh"  | grep -v "*sol.sh"  > list-of-sh2go-tasks-b.txt

