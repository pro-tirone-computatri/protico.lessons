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

EXC=sh2go-21
echo "executing Uebung $EXC"

# (1) Definieren Sie in diesem Script eine Variable VFATHER mit dem Wert Mother. 
# (2) Lassen Sie von diesem 'Father-Script' ein heredoc namens 'child.txt' auf die Platte schreiben, das
#     (a) seinerseits eine eigene Shebang-Zeile hat
#     (b) seinerseites eine Variable VCHILD="Daughter" definiert und
#     (c) per echo einen String der Form "$VCHILD grüßt $VFATHER zurück" ausgibt 
# (3) Lassen Sie vom 'Father-Script' aus ${VFATHER} per echo das Kind im 'Child-Skript' grüßen.
# (4) Rufen Sie dann vom 'Father-Script' per <bash child.txt> das 'Child-Skript' auf.
# (5) Sehen Sie, dass das Child-Skript die im Father-Script definierte Variable VFATHER nicht kennt.
# (5) Exportieren Sie dann im 'Father-Script' die Variable VFATHER.
# (6) Rufen Sie schießlich vom 'Father-Script' per <bash child.txt> das 'Child-Skript' auf.
# (7) Sehen Sie, dass das Child-Skript die im Father-Script definierte Variable VFATHER nun kennt.
#
# Hintergrund: 
#
# Ein Shell-Skript kann auch als Code-Generator benutzt werden: Der Code wird dann im übergeordneten
# bash-Skript zusammengestellt, durch Einbau von Variablen 'gecustomizet' und als Programm
# (hier: selbst wieder ein bash-Skript) auf den Datenträge geschrieben.
#
# Dabei sind 2 spezielle Dinge zu beachten:
#
# (A) Wenn das generierte Script selbst Variablen enthalten soll, muss der Variablenkenner - hier
#     - das $ vor dem Variablenname - ausmaskiert werden. Sonst würde das Code-Generator-Script
#     versuchen, die Variable selbst zu expandieren, anstatt das dem genrierten Script zu überlassen.
# (B) In einem Übergeordneten Script definierte Variablen sind NICHT automatisch von einem
#     untergeordneten Script aus zu erreichen. Wenn das möglich sein soll, müssen diese
#     Variablen mit dem Befehl <export VFATHER> exportiert werden, (und zwar ohne $, weil 
#     an dieser Stelle VFATHER ja nicht expandiert werden soll)


