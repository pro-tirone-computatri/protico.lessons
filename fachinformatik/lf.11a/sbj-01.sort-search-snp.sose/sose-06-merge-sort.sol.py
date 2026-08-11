#!/bin/sh
#
# This file is part of the Open Source project 'proTirone'
# (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
# It is distributed under the terms of the creative commons license
# CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
#

EXC="sose-05-merge-sort.py"
print(f"executing exercise <{EXC}>")

# Task
#
# (A) Implementieren Sie eine Funktion <merge_sort>: sie nehme die Liste 
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
#     Du bist ein Sortieragent und kannst beliebig viele andere Sortieragenten
#     mit Zuarbeiten beauftragen: Hat Deine Auftragsliste <= 1 Elemente, gib
#     sie als sortierte Liste zurück, ansonsten teile Deine Auftragsliste in 
#     zwei kleinere (möglichst gleich große) und beauftrage zwei andere Agenten 
#     mit deren Sortierung. Die beiden sortierten Ergebnislisten, die Dir Deine
#     Agent zurückgeben, sortierst Du nun in Deine Ergebnisliste und gibst
#     die als Resultat zurück.
#
#     Im Unterschied zum Quicksort machst Du Deine eigene Sortierarbeit
#     gewissermaßen auf dem "Rückweg": Du weißt jetzt, dass in jeder Ergebnisliste
#     alle tatsächlich nach dem ersten Element kommenden Element auch nach diesem
#     kommen sollen! Du kannst also solange die Elemente aus der einen Liste 
#     ohne Extraarbeit in die Zielliste übernehmen, bis Du auf dabei auf ein Element 
#     triffst, das nach dem ersten Element der anderen Teilliste kommen sollte. Dann
#     tauschst Du die Rollen Deiner Teillisten.
#
# Hintergrund: Der Merge-Sort denkt rekursiv:
#
# (1) Wenn die zu sortierenden Liste 1 Element enthält: 
#     gib sie als (von links nach rechts) sortiert zurück.
# (2) Wenn die zu sortierenden Liste > 1 Elemente enthält: 
#  a) teile die Liste in 2 Hälften
#  b) rufe den Merge-Sort für die linke Häfte aus und speichere die
#     zurückgegebenen Ergebnisse als 'sortierte linke Teilliste' [Rekursion 1]
#  c) rufe den Merge-Sort für die rechte Häfte aus und speichere die
#     zurückgegebenen Ergebnisse als 'sortierte rechte Teilliste' [Rekursion 2]
#  /* hier: allof(sortiere_linke_Teilliste) < allof(sortiere_rechte_Teilliste) 
#   * das muss das nun folgende Mergen sicherstellen 
#   */    
#  d) setze Übernahmekandidat-L auf das erste Element der sortierten linke Teilliste
#  e) setze Übernahmekandidat-R auf das erste Element der sortierten rechten Teilliste
#  f) initialiere die Rückgabeliste als leere Liste
#  g) solange es in beiden Teillisten noch Übernahmekandidaten gibt:
#   - Wenn Übernahmekandidat-L kleiner Übernahmekandidat-R:
#     - Hänge Übernahmekandidat-L an die Rückgabeliste an
#     - Setzte den Nachfolger von Übernahmekandidat-L als neuen Übernahmekandidat-L
#   - sonst
#     - Hänge Übernahmekandidat-R an die Rückgabeliste an
#     - Setzte den Nachfolger von Übernahmekandidat-R als neuen Übernahmekandidat-R
#  h) Gibt es noch Übernahmekandiaten in der sortierten linken Teilliste
#     hänge sie in dieser Reihenfolge an die Rückgabeliste an
#  i) Gibt es noch Übernahmekandiaten in der sortentierten rechten Teilliste
#     hänge sie in dieser Reihenfolge an die Rückgabeliste an
#  j) gib die Rückgabeliste zurück
# 
# (4) Bzgl. Python s. sose-02.py
# (5) Bzgl. des Datentyps Liste s. sose-02.py:

# freely following [https://www.datacamp.com/tutorial/python-merge-sort-tutorial]
# see also [https://de.wikipedia.org/wiki/Mergesort]


comparisons=0
sort_order={"7":0,"8":1,"9":2,"10":3,"B":4,"D":5,"K":6,"A":7}

# is element a 'lesser' than element b?
def is_lesser(elema,elemo):
  global comparisons
  global sort_order
  comparisons+=1

  if sort_order[elema]<sort_order[elemo]:
    return True
  else:
    return False

# the function required by the task. returns number of sorted cards
def merge_sort(list_to_be_sorted):
  # if list_to_be_sorted has only one or 0 members, it is sorted => nothing todo
  # if list_to_be_sorted has more than 1 member, we must sort the list
  if len(list_to_be_sorted) > 1: 
    # split part
    mid = len(list_to_be_sorted)//2
    left_half = list_to_be_sorted[:mid]
    right_half = list_to_be_sorted[mid:]
       
    #recursion
    merge_sort(left_half)
    merge_sort(right_half)

    # merge part
    ltoc=0 # left take over candidate
    rtoc=0 # right take over candidate

    here = 0
 
    while ltoc < len(left_half) and rtoc < len(right_half):
      if is_lesser(left_half[ltoc],right_half[rtoc]):
        list_to_be_sorted[here] = left_half[ltoc]               
        ltoc += 1
      else:
        list_to_be_sorted[here] = right_half[rtoc]
        rtoc += 1
      here += 1
     
      while ltoc < len(left_half):
        list_to_be_sorted[here] = left_half[ltoc]
        ltoc += 1
        here += 1
 
      while rtoc < len(right_half):
        list_to_be_sorted[here] = right_half[rtoc]
        rtoc += 1
        here += 1

#main

#chaosl=["7","8","9","10","B","D","K","A"]
#chaosl=["A","K","D","B","10","9","8","7"]
chaosl=["7","A","B","K","9","D","8","10"]

merge_sort(chaosl)
print(f"{chaosl} sorted by using {comparisons} comparisons")