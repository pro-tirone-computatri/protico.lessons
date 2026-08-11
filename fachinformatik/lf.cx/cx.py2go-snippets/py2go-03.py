# (C) 2025 K.Reincke: proTirone snippet [CC-BY-4.0]
'''
1. Weisen Sie einer Variable myName Ihren Vornamen und Namen als String zu.
2. Weisen Sie einer Variable my_age Ihr Alter zu.
3. Lassen sie mit allen drei Möglichkeiten den Satz ausgeben: 
   "Ich, Karsten Reincke, bin 67 Jahre alt".


Sie haben in Python 3 Möglichkeiten, einen String auszugeben, der auf Werten von Variablen zugreift:
a. Sie lassen print hintereinander übergebene Werten ausgeben, z.B.
   myZahl = 42
   print("Ich liebe die Zahl ", myZahl). 
   Das ist sperrig und endet oft unschön.
b. Sie können den Einbau der Werte in einen String einer Methode 'format' übergeben
   print("Ich liebe der Zahl {}".format(myZahl))
   Das ist elegant. 
   Man muss nur aufpassen, dass man der Methode die Werte in der richtigen Reihenfolge übergibt
c. Sie können einen f-String verwenden:
   print(f"Ich liebe die Zahl {myZahl}")
   Hier können Sie die Variablen direkt an der Stelle schreiben, wo ihr Wert ausgegeben werden soll.
d. C/C++ und Java liebe capitalized Variablen (myName). Die Pythone-Community bevorzugt nUnterstriche.
   Sie sehen, dass das technisch gesehen bloßer Style ist. Trotzdem ist es wichtig, um sich als Experte zu zeigen.
'''

