#!/bin/sh
#
# This file is part of the Open Source project 'proTirone'
# (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
# It is distributed under the terms of the creative commons license
# CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
#

EXC="sose-01-binary-search-iterative.py"
print(f"executing exercise <{EXC}>")

# Task
#
# (A) Implementieren Sie eine Funktion <binary_search> im iterativen Stil: 
#     sie nehme den aufsteigend sortierten Kartenstapel (Liste) 
#     sortl=["7","8","9","10","B","D","K","A"] und eine beliebige Karte und
#     liefere, falls letztere enthalten ist, deren Position (0 < n), sonst -1
# 
# (B) Implementieren Sie im main-Bereich damit eine Suche nach der Karte "K"
#
# (C) Zählen Sie die Anzahl der Vergleiche, bis Sie das Elemente gefunden haben,
#    und geben Sie eine entsprechende Statistik aus
#
# Hintergrund: 
#
# (1) Die binäre Suche setzt voraus, dass der Suchraum sortiert ist und dass
#     sie die Regeln der Sortierung kennt.Sie agiert so:
# (2) Die Idee ist, dass die Suchfunktion im Wissen um die Sortierreihenfolge
#     nur noch dort sucht, wo sich das zu suchenden Element noch befinden kann.
#     Das reduziert die Anzahl der Suchschritte
# 
# (3) Es gibt 2 Arten, das zu implementieren: A) iterativ und B) rekursiv.
#
# (A) iterativ:
#
# (a) setze initial die untere Grenze des Suchbereichs auf Indexzahl des ersten
#     zu vergleichenden Elements (meist: 0)
# (b) setze initial die obere Grenze des Suchbereichs auf die Indexzahl des 
#     letzten noch zu vergleichenden Elements (meist: Listenlänge-1)
# (c) programmiere eine Schleife, die solange läuft bis, die untere Grenze 
#     an der oberen vorbeigelaufen ist (= solange es im Suchbereich noch ein 
#     zu vergleichendes Element gibt)
# (d) und deren Schleifenkörper
#     - die Indexzahl des mittigen Elements im Suchbereich berechnet
#     - Erfolg meldet, sofern das mittige Element dem gesuchten gleicht,
#     - den Suchbereich auf den Bereich rechts vom mittigen Element eingrenzt
#       (untere Grenze auf Indexzahl des mittigen Elements +1 setzen),
#       sofern das mittige Element kleiner als das gesuchte ist
#     - den Suchbereich auf den Bereich links vom mittigen Element eingrenzt
#     - die nächsten Schleifendurchgang startet


comparisons=0

# dictionary determining the sort order: 
# get the sort position of the card as value of the card as key
sort_order={"7":0,"8":1,"9":2,"10":3,"B":4,"D":5,"K":6,"A":7}

# is element a 'lesser' than element b?
def is_before(elema,elemo):
  global sort_order

  if sort_order[elema]<sort_order[elemo]:
    return True
  else:
    return False

# the requested iterative binary search function
def binary_search(slist,sstart, send, selem):
  global comparisons
  global sort_order

  while sstart <= send:
    comparisons+=1                      # each loop is a search step

    midind=(sstart+send)//2

    if (slist[midind]==selem):
      return midind

    if is_before(selem,slist[midind]): # focus on left part
      send=midind-1
    else:                              # focus on right part 
      sstart=midind+1
    # next loop with 'shifted' search erea
  
  return -1

# main

# the sorted card stack
sortl=["7","8","9","10","B","D","K","A"] 
searchfor="K"

position=binary_search(sortl,0,len(sortl)-1,searchfor)

if (position==-1):
  print(f"{sortl} does not contain an element <{searchfor}>")
else:
  print(f"At index number {position}, list {sortl} contains <{searchfor}> as its {position+1}th element")
  print(f"found <{searchfor}> by using {comparisons} comparisons")