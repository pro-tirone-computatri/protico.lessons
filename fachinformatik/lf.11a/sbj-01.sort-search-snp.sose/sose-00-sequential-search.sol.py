#!/bin/sh
#
# This file is part of the Open Source project 'proTirone'
# (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
# It is distributed under the terms of the creative commons license
# CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
#

EXC="sose-00-sequential-search.py"
print(f"executing exercise <{EXC}>")

# Task
#
# (A) Implementieren Sie eine Funktion <linear_search>: sie nehme den unsortierten
#     Kartenstapel (vom Typ Tupel) chaost=("7","A","B","K","9","D","8","10") und
#     eine beliebige Karte und liefere, falls letztere enthalten ist, 
#     deren Position (0 < n), sonst eine -1
# 
# (B) Implementieren Sie im main-Bereich damit eine Suche nach der Karte "K"
#
# (C) Zählen Sie die Anzahl der Vergleiche, bis Sie das Elemente gefunden haben,
#    und geben Sie eine entsprechende Statistik aus
#
# Hintergrund: 
#
# (1) Wenn Sie einen Datenhaufen haben und nichts über dessen innere Ordnungs-
#     struktur wissen, bleibt Ihnen nichts anderes, als den Haufen der Reihe nach 
#     (= sequentiell bzw. linear) durchzugehen und solange jedes Element mit 
#     dem gesuchten zu vergleichen, bis eines dem gesuchten gleicht.
# (2) Was die Bedingungen sind, dass etwas dem anderen gleicht, hängt von der
#     Domäne ab und kann mit einer Funktion 'equals' gesondert implementiert
#     werden. Hier reicht der übliche Vergleich '='

comparisons=0

def linear_search(str_tuple,str_element):
  global comparisons
  position=0
  while (position<len(str_tuple)):
    comparisons+=1
    if (str_tuple[position]==str_element):
      return position
    position+=1

  return -1


chaost=("7","A","B","K","9","D","8","10")
searchfor="K"
position=linear_search(chaost,searchfor)

if (position==-1):
  print(f"{chaot} does not contain an element <{searchfor}>")
else:
  print(f"At index position {position}, {chaost} contains <{searchfor}> as its {position+1}th element")

print(f"found <{searchfor}> by using {comparisons} comparisons")