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

EXC=sh2go-03
echo "executing Uebung $EXC"

# (1) Geben Sie das 1., 2. und 3. Kommandozeilenargument aus.  
# (2) Geben Sie die Anzahl der Kommandozeilenargumente aus.
# (3) Rufen Sie diese Skript mit <sh3go-03-var.sh Good Morning> auf

# Hintergrund: 
#
# (A) Übergibt man einem Shellskript n Argumente / Parameter an der Kommandozeile
#     kann das Skript diese als Variablen $0 $1 ... $n benutzen
# (B) $0 ist immer der Skriptname selbst
# (C) $# ist die Anzahl der übergebenen Argumente OHNE den Skriptnamen mitzuzählen
#
# Extrahinweis: Wenn Sie das Zeichen $ selbst ausgeben wollen,
# können Sie in den String \$ schreiben


echo "\$0: $0"
echo "\$1: $1"
echo "\$2: $2"
echo "\$#: $#"



