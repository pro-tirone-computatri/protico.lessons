#!/bin/sh
#
# This file is part of the Open Source project 'proTirone'
# (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
# It is distributed under the terms of the creative commons license
# CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
#

EXC="sose-03i-selection-sort.py"
print(f"executing exercise <{EXC}>")

# Task
#
# (A) Implementieren Sie eine Funktion <selection_sort>: sie nehme die Liste 
#     chaosl=["7","A","B","K","9","D","8","10"] mit Spielkarten und liefere eine 
#     aufsteigend sortierte Liste <sortl> mit den Elementen aus chaosl zurück. 
#     chaosl sei am Ende leer
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
#     Suche immer wieder das kleinste Element aus der Liste der noch einzusortierenden
#     Elemente heraus und hänge es an die Liste der sortierten an.
#
# Hintergrund: 
#
# (1) Der Selection-Sort durchsucht die unsortierte Liste immer wieder nach dem 
#     Element, das von den in der Liste verbliebenen Elementen gemäß der 
#     intendierten Sortierreihenfolge als erstes kommen müsste. Hat der aktuelle 
#     Durchgang des Selection-Sorts das nächste 'erste Element' gefunden, entfernt 
#     er es aus der unsortierten Liste, hängt an das Ende der sortierten Liste
#     und started den nächsten Durchgang. Das wiederholt er, bis die Liste leer ist.
#
# (2) Die Entscheidung, ob ein Element vor einem anderen einzusortieren ist, 
#     soll an eine Einscheidungsfunktion delegiert werden, die <true> bzw. <false>
#     zurückliefert. (Ein gängiges Beispiel wäre der Test '<' )
#     
# (3) Bzgl. Python s. sose-02.py
# (4) Bzgl. des Datentyps Liste s. sose-02.py:

