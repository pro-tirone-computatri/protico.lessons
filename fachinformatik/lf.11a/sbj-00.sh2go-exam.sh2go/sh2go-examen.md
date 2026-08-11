<!-- LTeX:Language=de-DE -->

# Klausur

## Lehrervorbereitung:

Erzeugen Sie aus der Datei `xcolors-simple.md` 15 Zettel mit Farbnamen.
Nehmen Sie die mit einem ! versehenen Farben. Hat Ihre Klasse mehr als 15
Teilnehmer, leiten Sie aus der Datei xaa.txt genügend zusätzliche Dateien 
ab, fügen Sie diese unter einem je neuen Dateinamen in den Dateibau ein 
und ersetzen Sie in diesen Dateien jeweils der Farbcode durch einen der
unbenutzten aus der Liste (ohne !).

Geben Sie vor der Klausur jedem Schüler einen Zettel mit 'seiner' Farbe.

## Schüleranweisung:

Bitte laden Sie sich das tar.gz-Paket mit den bekannten Snippets und 
den Klausuraufgaben herunter, entpacken Sie es in einem Ordner, in und mit 
dem Sie ihre Linuxtools von der Bash aus erreichen.

### **(I)** 

Lösen Sie diejenigen Skriptaufgaben aus dem Ordner `snp.sh2go` auf die bekannte Weise,
zu denen noch keine Lösungsdatei mitgeliefert ist. [2 PT pro Lösung]

### **(II)** 

Im Ordner `exam.sh2go` finden Sie einen Ordner `xcolor-branded-files` und vier
Shell-Script-Aufgaben `sh2go-exam-a.sh`, `sh2go-exam-b.sh`, `sh2go-exam-c.sh`
und `sh2go-exam-d.sh` - jeweils ohne entsprechende Lösungsdatei. Die sollen Sie
programmieren. 

Die Aufgabendateien enthalten Aufgabentext und Lösungshinweise. Bitte

* kopieren Sie das Aufgabenskript unter dem mit `.sol` und Ihrem Namen erweiterten Dateinamen,  
  z.B. `sh2go-exam-a` `->` `sh2go-exam-a.sol.karsten-reincke.sh`
* programmieren Sie Ihre Lösung in dieser Datei
* laden Sie Ihre Lösung in den bekannten Ordner hoch.

Hier die Aufgaben im Überblick:

---

* _Aufgabe **A**_ [PT 5]: Schreiben Sie ein bash-Skript,
  * das a) alle Dateien samt Pfad aus dem Ordner <xcolor-branded-files> auflistet und 
  * das b) (nur) unter dem Listeneintrag den Code `#xc-IHREFARBE` ausgibt, der zu
    der von Ihnen anfangs gezogenen Farbe passt und der in der entsprechende Datei 
    auch vorkommt.

---

<br ><br >

---

* _Aufgabe **B**_ [PT 5]: Schreiben Sie ein bash-Skript, das 
  * eine Liste aller in o.a. Dateien nach diesem Muster encodierten verwendete Farben ermittelt,
  * die Farben vom Enkodierungspräfix `#xc-` befreit
  * die Farben bereinigt in eine Listendatei schreibt und
  * diese Liste bei jedem Durchlauf neu initialisiert 

---

* _Aufgabe **C.1**_ [PT 3]: Schreiben Sie ein bash-Skript, das aus den o.a. Dateien die Farbstrings 
  heraussucht, die die Groß-Klein-Schreibung bei der Farbcodierung NICHT beachten 
  (z.B. `Xc-Farbe`) 

* _Aufgabe **C.2**_ [PT 5]: Erweitern Sie Ihr bash-Skript so, dass es 
  * a) aus den o.a. Dateien die Farbstrings heraussucht, die die Groß-Klein-Schreibung
    bei der Farbcodierung NICHT beachten (z.B. `Xc-Farbe`) 
  * b) Pfad und Dateinamen derjenigen Dateien ausgibt, die falschem Farbcode enthalten
  * c) unter jedem Dateinamen mit falschem Farbcode den enthalten falschen Farbcode
    ausgibt.

---

* _Aufgabe **D.1**_ [PT 3]: **_Konzipieren_** Sie ein Skript, das überprüft, ob alle sh2go-Übungen 
  intern auch die Übungsnummer verwenden, die extern ihr Dateinamen enthält
  Schreiben Sie Ihren Algorithmus als Kommentar über die Implementierung.

* _Aufgabe **D.2**_ [PT 5]: **_Implementieren_** Sie ein Skript, das überprüft, ob alle sh2go-Übungen 
  intern auch die Übungsnummer verwenden, die extern ihr Dateinamen enthält
  Wenn nicht, soll es Pfad und Namen der entsprechenden Datei und den
  Hinweis 'Mismatch' ausgeben

---

**Bewertung**

Bei den Aufgabe A - D aus Sektion (II) sind maximal 26 Punkte möglich. 
Bei 18 Punkten gibt es eine 2, bei 14 Punkten eine 3 und bei 11 Punkten eine 4. 
Ab 22 Punkte gibt es eine 1.

Im Einzelnen bewerte ich jede Aufgabe nach dem Prinzip:

1. Funktioniert der Code = (2 Punkte)
2. Ist er aussagekräftig kommentiert = (2 Punkte)
3. Ist er elegant geschrieben = (1-2 Extrapunkte)

Die gelösten Aufgaben aus Sektion (II) bringen Ausgleichspunkte