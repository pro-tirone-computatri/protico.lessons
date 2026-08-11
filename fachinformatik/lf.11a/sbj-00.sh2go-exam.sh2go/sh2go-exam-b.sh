#!/bin/sh
#
# This file is part of the Open Source project 'proTirone'
# (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
# It is distributed under the terms of the creative commons license
# CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
#

EXC=sh2go-exam-b
echo "executing solution of task <$EXC>"

# Im Arbeitsordner mit dieser Aufgabe befindet sich ein Unterordner namens
# `xcolor-branded-files`. Er enthält eine Reihe von Dateien, die in unterschiedlich
# tief verschachtelten Ordnern abgelegt sind.
#
# Die Dateien enthalten jeweils eine Zeile, die nur das Präfix #xc- plus einen
# Farbnamen enthält, z.B. `#xc-Blackblue`. Sie selbst haben zu Beginn der Klausur 
# Ihren Zettel mit Farbnamen (ohne Präfix) gezogen.


# EXAM-B: Schreiben Sie ein bash-Skript, das 
# a) eine Liste aller in o.a. Dateien nach diesem Muster encodierten verwendete Farben ermittelt,
# b) die Farben vom Enkodierungspräfix `#xc-` befreit
# c) die Farben bereinigt in eine Listendatei schreibt und
# d) diese Liste bei jedem Durchlauf neu initialisiert 

# Hinweis: Hier könnte es hilfreich sein,`sh2go-04-backticks.sol.sh` zu Rate zu ziehen.

# [PT 5] 

MF="xcolors-used.txt"
if [ -f $MF ]; then rm $MF; fi
find xcolor-branded-files -type f | while read f; do \
  echo $f;
  colorline=`grep "#xc-" $f | sed "s/#xc-//"`;
  if [ "$colorline" != "" ]; then echo "$colorline" >> $MF; fi;
done
