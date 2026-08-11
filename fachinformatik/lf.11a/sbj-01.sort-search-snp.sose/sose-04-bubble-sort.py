#!/bin/sh
#
# This file is part of the Open Source project 'proTirone'
# (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
# It is distributed under the terms of the creative commons license
# CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
#

EXC="sose-04-bubble-sort.py"
print(f"executing exercise <{EXC}>")

# Task
#
# (A) Implementieren Sie eine Funktion <bublle_sort>: sie nehme die Liste 
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
#     Gehe den Stapel der zu sortierenden Elemente immer wieder von vorne durch 
#     und tausche die benachbarten Karten miteinander, die in der falschen
#     Reihenfolge stehen. Musstest Du keine Karten mehr tauschen, bist Du fertig.
#
# Hintergrund: 
#
# (1) Der Bubble-Sort verändert eine Liste solange, bis sie sortiert ist.
#     Er nimmt die einzusortierenden Karten/Elemente nicht von einem anderen 
#     Stack / aus einer anderen Liste.
# (2) Er durchläuft die zu sortierenden Liste solange immer wieder,
#     bis sie sortiert ist.
# (3) Bei jedem Durchgang tauscht er suzzessive Vorgänger und Nachfolger
#     aus, wenn sie in der falschen Reihenfolge stehen.
# 
# Dahinter steht die Idee, die Elemente von unten nach oben an ihre richtige
# Position aufsteigen zu lassen. Deshalb Bubble-Sort 
#     
# (4) Bzgl. Python s. sose-02.py
# (5) Bzgl. des Datentyps Liste s. sose-02.py:

