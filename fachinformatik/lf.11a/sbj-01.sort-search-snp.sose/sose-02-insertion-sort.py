#!/bin/sh
#
# This file is part of the Open Source project 'proTirone'
# (c) 2025 Karsten Reincke (https://github.com/protirone/protico.ltx)
# It is distributed under the terms of the creative commons license
# CC-BY-4.0 (= https://creativecommons.org/licenses/by/4.0/)
#

EXC="sose-02-insertion-sort.py"
print(f"executing exercise <{EXC}>")

# Task
#
# (A) Implementieren Sie eine Funktion <insertion_sort>: sie nehme die Liste 
#     chaosl=["7","A","B","K","9","D","8","10"] mit Spielkarten und liefere eine 
#     aufsteigend sortierte Liste <sortl> mit den Elementen aus chaosl zurück. 
#     chaosl sei am Ende leer
# 
# (B) Implementieren Sie dazu eine Vergleichsfunktion, die das Dictionary
#     ref_dict={"7":0,"8":1,"9":2,"10":3,"B":4,"D":5,"K":6,"A":7} als
#     Vergleichsmaßstab benutzt.
#
# (C) Notieren/Zählen Sie, wieviele (Vergleichs)Schritte Sie zum Herausnehmen der 
#     einzusortierenden Elemente benötigen und wieviele (Vergleichs)Schritte
#     Sie zum Einsortieren der Elemente benötigen.
#
# Grundidee:
#
#     Nimm immer wieder das oberste Element vom Stapel der einzusortierenden und 
#     gehe den Stapel der schon sortierten bis zu dem Element durch, das nach
#     dem neu einzusortierenden kommen müsste. Sortiere das neu einzusortierende
#     direkt davor ein.
#
# Hintergrund: 
#
# (1) Der Insertion-Sort nimmt die einzusortierenden Elemente der Reihe nach
#     von einem Stapel und geht die bereits einsortierten Elemente von vorn an
#     bis zu dem ersten Element durch, das nach dem vom Stapel genommenen
#     Element einzuordnen wäre. Direkt davor sortiert er das neue Element ein.
#     
#     Sonderfälle: 
#
#     a) Ist der Zielstapel noch leer, wird das neu einzusortierende eingefügt.
# 
#     b) Wenn schon das erste der bereits einsortierten Elemente NACH dem neu 
#     einzusortierenden kommen sollte, wird das neu einzusortierende am Anfang 
#     eingefügt.
#
#     c) Wenn auch das letzte der bereits einsortierten Elemente noch VOR dem 
#     neu einzusortierenden käme, wird das neu einzusortierende am Ende angehängt.
#
# (2) Die Entscheidung, ob ein Element vor einem anderen einzusortieren ist, 
#     soll an eine Einscheidungsfunktion delegiert werden, die <true> bzw. <false>
#     zurückliefert. (Ein gängiges Beispiel wäre der Test '<' )
#     
# (3) Python kennt (nativ) als 'Werte-Container' nur Strings, Listen, Tupel und
#     Dictionaries (= Hashmaps). Arrays im traditionellen Sinne gibt es in Python 
#     nicht. Allerding werden in Python die Typen nicht explizit angegeben. 
#     Die Zuweisungnotation an sich entscheidet schon über den Typ:
#
#     a) CARD_STRING="789aBDKA"
#     b) CARD_TUPLE=("7","8","9","10","B","D","K","A")
#     c) CARD_LIST=["7","8","9","10","B","D","K","A"]
#     d) CARD_DICT={0:"7",1:"8",2:"9",3:"10",4:"B",5:"D",6:"K",7:"A"}
#
#     Einzelne Elemente von CARD_STRING, CARD_TUPLE oder CARD_LIST können 
#     mit der Indexnotation - wie z.B. CARD_TUPLE[4] abgerufen werden. Deshalb
#     gelten diese Typen als die sequentiellen Datentypen von Python.
#
#     Dass ein solcher Abruf hier auch für CARD_DICT funktioniert, ist zufällig
#     und liegt daran, dass wir als Key die Indexnummer genommen haben
# 
# (4) Der Python-Datentyp <Tuple> kann nicht verändert werden: Sie können den
#     Wert eines eingefügten Elements nachträglich nicht ändern und auch keine
#     anderen Elemente hinzufügen oder löschen
#
# (5) Der Datentyp Liste bietet die Methoden:
#     - list.append(element) /* hängt 'element' an 'liste' an */
#     - list.remove(element) /* entfernt 'element' aus der 'liste', wo immer es steht */
#     - list[i]     /* gibt element an Position i zurück */
#     - list.pop(0) /* gibt erstes element zurück und entfernt es aus der Liste */
#     - list.insert(i,element) /* fügt element an Position i in die Liste ein*/

