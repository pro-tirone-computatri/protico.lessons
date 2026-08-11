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
