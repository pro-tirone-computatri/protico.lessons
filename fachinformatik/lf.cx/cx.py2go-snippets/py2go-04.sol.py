# (C) 2025 K.Reincke: proTirone snippet [CC-BY-4.0]
'''
1. Weisen Sie einer Variable my_first_name Ihren Vornamen zu.
2. Weisen Sie einer Variable my_last_name Ihren Nachnamen zu.
3. Weisen Sie einer Variable my_age Ihr Alter zu.
4a. Initialisieren Sie die Variable mea so, dass sie einen String der Form
   "Ich,  Karsten Reincke, 67 , programmiere gerade"
   enthält. Nutzen Sie dazu die Stringkonkatenationsfunktion '+'
4b. Initialisieren Sie die Variable meb so, dass sie einen String der Form
   "Ich,  Karsten Reincke, 67 , programmiere gerade"
   enthält. Nutzen Sie dazu einen f-String (Methode 3 aus py2go-03)
4c. Geben Sie die Strings mea und meb mit print aus.
5. Initialisieren Sie als Gegenprobe die Variablen mec und med mit den beiden
   anderen Methoden aus py2go-03 und gegeben Sie sie mit print aus. Es werden
   Arrays ausgegeben, keine Strings. Das zeugt, warum Sie sie nicht zum Zweck
   der Stringbildung nutzen können.

Hinweis:

Von den Methoden der Stringzusammensetzung aus py2go-03 können Sie regulär nur 
die Methode 3 anwenden.

my_firstname="Karsten"
mec=(f"Ich heiße {my_first_name}")

Dafür können Sie als 2. Variante den Konketantionsoperator '+' verwenden:

med="Ich heiße " + my_first_name


'''

my_first_name="Karsten"
my_last_name="Reincke"
my_age=67

meb=(f"Ich, {my_first_name} {my_last_name}, {my_age}, programmiere gerade")
mea="Ich ,"+ my_first_name + " " + my_last_name + ", " + str(my_age) + ", programmiere gerade."

mec="Ich,{} {}, {}, programmiere gerade",my_first_name,my_last_name,my_age
med="Ich ,",my_first_name," ",my_last_name,", ",str(my_age),", programmiere gerade."

print(mea)
print(meb)
print(mec) 
print(med)