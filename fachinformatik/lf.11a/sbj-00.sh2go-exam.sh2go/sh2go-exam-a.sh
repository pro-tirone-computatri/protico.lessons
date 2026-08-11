#!/bin/sh
#
# This file is part of the Open Source project 'proTirone'
# (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
# It is distributed under the terms of the creative commons license
# CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
#

EXC=sh2go-exam-a
echo "executing solution of task <$EXC>"

# Im Arbeitsordner mit dieser Aufgabe befindet sich ein Unterordner namens
# `xcolor-branded-files`. Er enthält eine Reihe von Dateien, die in unterschiedlich
# tief verschachtelten Ordnern abgelegt sind.
#
# Die Dateien enthalten jeweils eine Zeile, die nur das Präfix #xc- plus einen
# Farbnamen enthält, z.B. `#xc-Blackblue`. Sie selbst haben zu Beginn der Klausur 
# Ihren Zettel mit Farbnamen (ohne Präfix) gezogen.


# EXAM-A: Schreiben Sie ein bash-Skript,  
# das a) alle Dateien samt Pfad aus dem Ordner <xcolor-branded-files> auflistet und 
# das b) (nur) unter dem Listeneintrag den Code `#xc-IHREFARBE` ausgibt, der zu
# der von Ihnen anfangs gezogenen Farbe passt und der in der entsprechende Datei 
# auch vorkommt.

# Hinweis: Hier könnte es hilfreich sein, `sh2go-04-backticks.sol.sh` und 
# `sh2go-11-if.sol.sh` zu Rate zu ziehen

# [ PT 5]

find xcolor-branded-files -type f | while read f; do \
  echo $f;
  colorline=`grep "#xc-" $f`;
  if [ "$colorline" = "#xc-Green" ]; then echo "$colorline"; fi;
done

   