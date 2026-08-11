#!/bin/sh
#
# This file is part of the Open Source project 'proTirone'
# (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
# It is distributed under the terms of the creative commons license
# CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
#

EXC=sh2go-exam-d
echo "executing solution of task <$EXC>"

# Im Lernscriptordner neben dieser Aufgabe <../snp.sh2go> finden Sie die Ihnen
# bekannten Übungen. Jede Übung enthält einen Identifier, enkodiert nach dem
# Muster 'EXC=sh2go-01'. Mit diesem Identifier sollte auch der Dateiname
# der Übung beginnen.

# EXAM-D1: Konzipieren Sie ein Skript, das überprüft, ob alle sh2go-Übungen 
# intern auch die Übungsnummer verwenden, die extern ihr Dateinamen enthält
# Schreiben Sie Ihren Algorithmus als Kommentar über die Implementierung.

# [3 PT]

# EXAM-D2: Implementieren Sie ein Skript, das überprüft, ob alle sh2go-Übungen 
# intern auch die Übungsnummer verwenden, die extern ihr Dateinamen enthält
# Wenn nicht, soll es Pfad und Namen der entsprechenden Datei und den
# Hinweis 'Mismatch' ausgeben

# [5 PT]

# describing the algoriothm
# 1. Finde alle sh2go-Dateien
# 2. Fische die externe Nummer aus dem Dateinamen mit sed
# 3. Fische die interne Nummer aus der Datei mit grep und sed
# 4. Vergleiche die Nummern. Sind sie verschiedenen
#    gibt den Dateinamen und den String MISMATCH aus

find ../snp.sh2go -name "sh2go-*.sh" | while read f; do \
  echo $f;
  NUM_IN_FILENAME=`echo $f | sed "s/.*\(sh2go-[0-9][0-9]*\)-.*.sh/\1/"`
  NUM_IN_FILECONTENT=`grep "EXC=" $f | sed "s/EXC=//"`
  if [ $NUM_IN_FILENAME != $NUM_IN_FILECONTENT ]; then 
    echo "MISMATCH in $f";
    echo "compared <$NUM_IN_FILENAME> <$NUM_IN_FILECONTENT>"
  fi
done