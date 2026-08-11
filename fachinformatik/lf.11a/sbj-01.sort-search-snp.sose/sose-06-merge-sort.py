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
#
# freely following [https://www.datacamp.com/tutorial/python-merge-sort-tutorial]
# see also [https://de.wikipedia.org/wiki/Mergesort]