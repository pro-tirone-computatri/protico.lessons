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

EXC=sh2go-08
echo "executing Uebung $EXC"

# (1) Schreiben Sie das heutige Datum mit dem Format +'%Y%m%d" in eine Datei. Nutzen Sie dafür das Tool <date> 
# (2) Hängen Sie aus dem Skript heraus die Zeile '2024 war besser' an Ihre Datei
# (3) Lassen Sie aus dem Skript heraus die Zeile finden (herausgreppen), in der das Jahr 2025 vorkommt.
# (4) Lassen Sie aus dem Skript heraus die Zeile finden (herausgreppen), in der das Jahr 2024 vorkommt.
# (5) Formulieren Sie einen Suchparameter für 'grep', der grep beide Zeilen finden lässt.

# Hintergrund: 
#
# (A) Zum Such von Zeilen, die ein Suchmuster enthalten, ist das Tool <grep> zuständig.
# (b) <grep> nimmt einen regulären Ausdruck (RegEx) und einen Dateinamen (oder einen Zeileninhalt) 
#     und gibt die Zeile aus, die den regulären Ausdruck erfüllt.

# a) ein literaler String ist ein RegEx, z.B. '2023'
# b) Varianten an einer Position im RegEx werden in eckigen Klammern hintereinander geschrieben:
#    a[bc]a beschreibt aba oder aca aber nicht abca ...
# c) Soll ein Buchstabe oder eine Zahl mehrfach hintereinander vorkommen, wird er quantifiziert
#    mit + oder * (+ :- 1 oder mehrmals, * 0 oder mehrmals)

echo `date +'%Y%m%d'` > mf.txt
echo '2024 war besser' >> mf.txt
grep '2025' mf.txt
grep '2024' mf.txt
grep '202[45]' mf.txt
