#!/bin/sh
#
# This file is part of the Open Source project 'proTirone'
# (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
# It is distributed under the terms of the creative commons license
# CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
#

EXC="sose-06-quick-sort.py"
print(f"executing exercise <{EXC}>")

# Task
#
# (A) Implementieren Sie eine Funktion <quick_sort>: sie nehme die Liste 
#     chaosl=["7","A","B","K","9","D","8","10"] mit Spielkarten und liefere eine 
#     aufsteigend sortierte Liste <sortl> mit den Elementen aus chaosl zurück. 
# 
# (B) Nutzen Sie dazu Ihre schon implementierte eine Vergleichsfunktion, die das 
#     Dictionary ref_dict={"7":0,"8":1,"9":2,"10":3,"B":4,"D":5,"K":6,"A":7} als
#     Vergleichsmaßstab benutzt.
#
# (C) Notieren/Zählen Sie, wieviele (Vergleichs)Schritte Sie zum Herausnehmen der 
#     einzusortierenden Elemente benötigen und wieviele (Vergleichs)Schritte
#     Sie zum Einsortieren der Elemente benötigen.
#
# Grundidee:
#
#     Du bist ein intelligenter Sortieragent und kannst beliebig viele andere 
#     intelligente Sortieragenten mit Zuarbeiten beauftragen: Hat Deine 
#     Auftragsliste <= 1 Elemente, gib sie als sortierte Liste zurück. Ansonsten 
#     suche Dir ein vom Wertebereich Deiner Auftragsliste möglichst mittig liegendes
#     Vergleichselement und sortiere Deine Auftragsliste in zwei Teillisten:
#     die eine enthält die kleineren Elemente, die andere die anderen. Beauftrage 
#     nun zwei andere Agenten mit deren Sortierung. Die sortierte Ergebnisliste,
#     die Dir Dein Agent zurückgibt, der die größeren Elemente sortieren sollte,
#     hängst Du nun einfach an die an, die Dir der Agent zurückgegeben hat, der
#     die kleinere sortieren sollte. Und das gibst Du als Dein Ergebnis zurück.
#
#     Im Unterschied zum Mergesort machst Du Deine eigene Sortierarbeit
#     schon auf dem "Hinweg": Deine Sub-Agenten bekommen Teilaufträge, die
#     unabhängig vom je anderen sortiert und danach wieder zusammengefügt werden 
#     können.
#
#     Die 'Intelligenz' von Euch Agenten besteht darin, schnell und ohne 
#     (versteckten) Zusatzaufwand ein gutes mittiges Vergleichselement (=
#     Pivotelement) zu finden.
#
# Hintergrund: Auch der Quick-Sort denkt rekursiv:
#
# (1) Wenn die zu sortierenden Liste 1 Element enthält, ist sie sortiert
# (2) Wenn die zu sortierenden Liste > 1 Elemente enthält: 
#  a) wähle ein passendes (etwa hälftiges) Vergleichselement (Pivotelement)
#  b) gehe die die zu sortierenden Liste durch
#   - ist das aktuelle Elemente kleiner als das Vergleichselement
#     übertrage es in die linke liste
#   - sonst
#     übertrage es in die rechte liste
#  c) rufe den Quick-Sort für die linke Häfte aus und speichere die
#     zurückgegebenen Ergebnisse als 'sortierte linke Teilliste' [Rekursion 1]
#  d) rufe den Quick-Sort für die rechte Häfte aus und speichere die
#     zurückgegebenen Ergebnisse als 'sortierte rechte Teilliste' [Rekursion 2]
#  /* hier: allof(sortiere_linke_Teilliste) < allof(sortiere_rechte_Teilliste) 
#   * das muss das nun folgende Mergen sicherstellen 
#   */    
#  e) hänge die sortierte rechte Teilliste an die sortiert linke Teilliste
#  f) gib das Ergebnis zurück
# (3) Bzgl. Python s. sose-02.py
# (4) Bzgl. des Datentyps Liste s. sose-02.py:

# Der Witz bei diesem Algorithmus ist es, das geeignete Pivotelement zu wählen.
# Bei dieser Kartenimplementierung kann der Index des Referenzarrayas 
# sort_oder halbiert und der entsprechende Wert als Pivotkarte genommen werden.

# see also [https://de.wikipedia.org/wiki/Quicksort]

comparisons=0
sort_order={"7":0,"8":1,"9":2,"10":3,"B":4,"D":5,"K":6,"A":7}
sort_index=["7","8","9","10","B","D","K","A"]

# is element a 'lesser' than element b?
def is_lesser(elema,elemo):
  global comparisons
  global sort_order
  comparisons+=1

  if sort_order[elema]<sort_order[elemo]:
    return True
  else:
    return False

def quick_sort(list_to_be_sorted,rl,rr):

  # a list of 0 or 1 elements is already sorted
  if len(list_to_be_sorted)<2: return list_to_be_sorted

  # the elements of an unordered list of 2 elements must be switched
  elif len(list_to_be_sorted)==2:
    # get the pair
    lm=list_to_be_sorted[0]
    rm=list_to_be_sorted[1]
    # if they are in the wrong order swap them
    if is_lesser(rm,lm):
      list_to_be_sorted[0]=rm
      list_to_be_sorted[1]=lm
    return list_to_be_sorted
  else:
    # compute the index of the next pivot element in the middle of the current range
    pivind=((rr-rl)//2)+rl
    pivcard=sort_index[pivind]
    #print(f"{rl}:{pivind}:{rr} = {pivcard} ")
    
    # for all members of the list to be sorted:
    i=0
    left_sub_list=[]
    right_sub_list=[]
    while i < len(list_to_be_sorted):
      # put them in the left list if they are 'lesser' than the pivot
      if is_lesser(list_to_be_sorted[i],pivcard):
        left_sub_list.append(list_to_be_sorted[i])
      # otherwise in the right list 
      else:
        right_sub_list.append(list_to_be_sorted[i])
      i+=1
    
    # recursion case

    return quick_sort(left_sub_list,rl,pivind-1)+quick_sort(right_sub_list,pivind,rr)

  
#main

#chaosl=["7","8","9","10","B","D","K","A"]
#chaosl=["A","K","D","B","10","9","8","7"]
chaosl=["7","A","B","K","9","D","8","10"]

sortl=quick_sort(chaosl,0,len(chaosl)-1)
print(f"{sortl} sorted by using {comparisons} comparisons")


