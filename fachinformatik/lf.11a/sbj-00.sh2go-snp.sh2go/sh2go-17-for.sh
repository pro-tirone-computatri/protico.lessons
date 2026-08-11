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

EXC=sh2go-17
echo "executing Uebung $EXC"

# Geben Sie alle möglichen Werte, die ein Byte annehmen kann, 
# mittels zweier for-Schleifen in einer Zeile als Hex-Werte aus.


# Hintergrund: 
#
# (a) Die Bash bietet auch eine For-Schleife
#     <for i in 1 2 3 4; do echo $i; done>
# (b) Die Iteratoren können auch als Range aufgelistet werden
#     <for i in {1..4}; do echo $i; done>
# (c) Die Iteratoren können auch als Variable übergeben werden.
#     ITE=`echo 1 2 3`
#     <for i in $ITE; do echo $i; done>
# (d) Default hängt echo an jede Ausgabe einen Zeilentrenner.
#     Will man mehrere Ausgaben in einer Zeile haben, nutzt
#     man mit der Option '-n' <echo -n 1> 
#
# Hinweis: Folgende Konstrukte führen NICHT zur iterierbaren Objekten:
#
# (x) ITE=1 2 3 wird interpretiert als ITE=1 + gefolgt von Kommando 2
# (y) ITE="1 2 3" wird als ein String interpretiert.

