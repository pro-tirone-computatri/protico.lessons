# (C) 2025 K.Reincke: proTirone snippet [CC-BY-4.0]

'''
1. Weisen Sie einer Variable 'number_a' den Wert 42 zu. 
2. Weisen Sie einer Variable 'number_b' den Wert 24 zu.
3. Überzeugen Sie sich mit der Funktion 'id', dass Sie unterschiedliche Objekt
   erhalten mit unterschiedlichen Werten haben.
4. Weisen Sie jetzt der Variable 'number_b' auch den Wert 42 zu.
5. Überzeugen Sie sich mit der Funktion 'id', dass Sie nun dieselben Objekte
   sind.
6. Erklären Sie sich, wie das sein kann.
7. Weisen Sie nun der Variable 'number_b' die Variable 'number_a' zu.
8. Überprüfen Sie, was sich zum Fall 4. 5. ändert.
9. Weisen Sie nun der Variable 'number_a' den Wert 13 zu. Überprüfen Sie,
   die Variablen 'number_a' und 'number_b' auf dasselbe Objekt zeigen
   oder nicht.

Hintergrund:

Der Zuweisungsoperator ist das einfache Gleichheitszeichen.

Andere Sprachen weisen einer Variable eine spezifische Speicherstelle zu und
vermerken den Typ, der zu dieser Speicherstelle gehört. Variable und
Speicherstelle bleiben verbunden (solange Sie nicht mit Pointerarithmetik 
manuell eingreifen.) [Statische Typedeklaration]

Python abstrahiert davon einen Schritt: [Dynamische Typedeklaration]

* Wenn sie einer Variable einen (bisher nicht verwendeten) Wert zuweisen, erzeugt 
  Python intern ein Objekt mit diesem Wert.
* Dann weist Python Ihrer Variable als Wert die Speicheradresse des Objektes zu.
* Fragen Sie nach dem Wert der Variable, liest Python den aus dem Objekt aus,
  ohne dass Sie etwas dafür tun müssten.
* Weisen Sie dann einer neuen Variable den schon verwendeten Wert zu, erzeugt
  Python kein neues Objekt, sondern weist Ihrer neuen Variable einfach die
  Speicheradresse des Objektes mit dem schon verwendeten Wert zu
* Die angelegten Objekte haben eine ID. Und die kann mit dem Operator id(VAR)
  abfragen, wobei VAR Ihre Variable im Quelltext ist.

Tests auf gleich und Ungleichheit schreiben Sie in Python als if-statement:

- Ein if-Statement startet mit der if-Clause (`if(TEST)`) gefolgt von enem Doppelpunkt.
- Ein Test ist ein Vergleich, der zu einem der Wahrheitswerte True oder False
  ausgewertet wird.
- Ergibt der Test den Wert 'True', werden die nachfolgenden Befehle ausgeführt,
  die nach dem Test um eine Einheit (2 Blanks oder 1 Tab oder 4 Blanks oder ...)
  eingerückt sind.
- Wollen Sie Befehle ausführen lassen, wenn der Test scheitert,
  hängen sie noch (uneingerückt) eine else-Zeile und ein oder mehrere
  eingrückte Befehle an.
- TESTs sind Vergleichsoperationen wie 
  - gleich '=='
  - ungleich '=='
  - größer '>'
  - kleiner '<'

Die weiter hineinkriechen wollen, mögen die Frage beantwortet, was passiert,
wenn man nach einer Zuweisung die ids nicht neu ermittelt. Kommentieren Sie
ihre entsprechenden Zeilen aus und probieren sie es aus.

'''
