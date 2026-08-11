#!/bin/sh
#
# This file is part of the Open Source project 'proTirone'
# (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
# It is distributed under the terms of the creative commons license
# CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
#

EXC="sose-01-binary-search-recursive.py"
print(f"executing exercise <{EXC}>")

# Task
#
# (A) Implementieren Sie eine Funktion <binary_search> im rekursiven Stil: 
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
# (B) rekursiv:
#
# (a) Der Funktion mögen als Parameter folgende Infos mitgegeben werden:
#     1. die zu durchsuchende Liste
#     2. das zu findende Element
#     3. die Indexzahl des ersten noch zu vergleichenden Elements
#     4. die Indexzahl des letzten noch zu vergleichenden Elements
# (b) Der Funktionskörper
#     - berechne die Indexzahl des mittigen Elements zwischen 
#       dem erstem und dem letztem Element, das noch verglichen werden soll
#     - melde Erfolg, sofern das mittige Element dem gesuchten gleicht, 
#       ( gebe dessen Indexzahl als Erfolg zurück)
#     - ermittelt, ob das mittige Element gemäß Sortierreihenfolge VOR dem 
#       gesuchten kommt, 
#     - wenn, ja, setze er den Nachfolger des mittigen Elements als neues 
#       erstes zu untersuchendes Element fest
#     - wenn nein, setze er den Vorgänger des mittigen Elements als neues 
#       letztes zu  untersuchendes Element fest
#     - rufe sich selbst als Funktion noch einmal mit den angepassten Parametern auf

comparisons=0

sort_order={"7":0,"8":1,"9":2,"10":3,"B":4,"D":5,"K":6,"A":7}

# is element a 'lesser' than element b?
def is_before(elema,elemo):
  global sort_order

  if sort_order[elema]<sort_order[elemo]:
    return True
  else:
    return False

# the requested recurive binary search function
def binary_search(slist,sstart, send, selem):
  global comparisons
  global sort_order
  comparisons+=1
  
  midind=(sstart+send)//2

  if (slist[midind]==selem):
      return midind

  if is_before(selem,slist[midind]): # focus on left part
    send=midind-1
  else:
    sstart=midind+1                 # focus on right part 

  # recursive call with 'shifted' search erea
  return binary_search(slist,sstart, send, selem)

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