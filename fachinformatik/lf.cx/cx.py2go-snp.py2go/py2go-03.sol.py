# (C) 2025 K.Reincke: proTirone snippet [CC-BY-4.0]
'''
1. Weisen Sie einer Variable myName Ihren Vornamen (= IHR_VORNAME) und Namen 
   (= IHR_NACHNAME) als String zu.
2. Weisen Sie einer Variable my_age Ihr Alter (= IHR_ALTER) zu.
3. Lassen Sie mit allen drei Python eigenen Möglichkeiten den Satz ausgeben: 
   "Ich, IHR_VORNAME IHR_NACHNAME, bin IHR_ALTER Jahre alt",
   wobei IHR_VORNAME, IHR_NACHNAME und IHR_ALTER in dieser Aufgabenbeschreibung
   eben für Ihren Vornamen, Namen und Alter stehe.


Hintergrund: 

Sie haben in Python 3 Möglichkeiten, einen String auszugeben, der auf Werten von 
Variablen zugreift:

a. Sie lassen print hintereinander übergebene Werte ausgeben, z.B.
     myZahl = 42
     print("Ich liebe die Zahl ", myZahl). 
   Das ist sperrig und endet oft unschön.

b. Sie können den Einbau der Werte in einen String einer Methode 'format' übergeben:
     print("Ich liebe der Zahl {}".format(myZahl))
   Das ist elegant. Man muss nur aufpassen, dass man der Methode format() die 
   Werte in der richtigen Reihenfolge übergibt

c. Sie können einen f-String verwenden:
     print(f"Ich liebe die Zahl {myZahl}")
   Hier können Sie die Variablen - in geschweiften Klammern - direkt an der Stelle 

   schreiben, wo ihr Wert ausgegeben werden soll.
d. C/C++ und Java lieben capitalized Variablen (myName). Die Pythone-Community 
   bevorzugt Unterstriche zur Trennung. 

   Um zu zeigen, dass das reiner Stil ist, verwenden wir hier 
   myName und my_age.

   Stil und Konventionen zu beachten ist trotzdem wichtig, um sich als Experte zu zeigen.

'''

myName="Karsten Reincke"
my_age=67

print("Ich,",myName,", bin jetzt",my_age,"Jahre alt")
print("Ich, {}, bin jetzt {} Jahre alt".format(myName,my_age))
print(f"Ich, {myName}, bin jetzt {my_age} Jahre alt")
