#!/bin/sh
#
# This file is part of the Open Source project 'proTirone'
# (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
# It is distributed under the terms of the creative commons license
# CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
#

EXC=sh2go-exam-c
echo "executing solution of task <$EXC>"

# Im Arbeitsordner mit dieser Aufgabe befindet sich ein Unterordner namens
# `xcolor-branded-files`. Er enthält eine Reihe von Dateien, die in unterschiedlich
# tief verschachtelten Ordnern abgelegt sind.
#
# Die Dateien enthalten jeweils eine Zeile, die nur das Präfix #xc- plus einen
# Farbnamen enthält, z.B. `#xc-Blackblue`. Sie selbst haben zu Beginn der Klausur 
# Ihren Zettel mit Farbnamen (ohne Präfix) gezogen.


# EXAM-C1: Schreiben Sie ein bash-Skript, das aus den o.a. Dateien die 
# Farbstrings heraussucht, die die Groß-Klein-Schreibung bei der Farbcodierung 
# NICHT beachten (z.B. `Xc-Farbe`) 

# Hinweise: Hier könnte es hilfreich sein, noch 'mal einen Blick in 
# `sh2go-08-grep.sol.sh` und in das Manual von grep hinsichtlich des Parameters 
# `-v` zu werfen

# [PT 3]

# EXAM-C2: Erweitern Sie Ihr bash-Skript so, dass es 
# a) aus den o.a. Dateien die Farbstrings heraussucht, die die Groß-Klein-Schreibung
#    bei der Farbcodierung NICHT beachten (z.B. `Xc-Farbe`) 
# b) Pfad und Dateinamen derjenigen Dateien ausgibt, die falschem Farbcode enthalten
# c) unter jedem Dateinamen mit falschem Farbcode den enthalten falschen Farbcode
#    ausgibt.

# [PT 5] 
echo "executing solution of task <$EXC>.1"

find xcolor-branded-files -type f | while read f; do 
  grep -i "#xc-" $f | grep -v "#xc-"
done

echo "executing solution of task <$EXC>.2"
find xcolor-branded-files -type f | while read f; do 
  colorline=`grep "#xc-" -i $f | grep -v "#xc-"`
  if [ "$colorline" != "" ]; then 
    echo $f;
    echo "$colorline";
  fi;
done