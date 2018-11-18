# Python Aufgaben

Die Schüler der 10. Klassen des Pythagoras-Gymnasiums haben verschiedene Kurse.
Ermittle, ob es Schüler gibt, die mit jedem anderen Schüler
der 10. Klasse zumindest einen gemeinsamen Kurs besuchen.


1. Lese die Datei pythagoras.txt so ein, dass in der globalen Variablen `kurse` 
alle Kurse mit ihren Teilnehmern als Liste vorliegen. `kurse` soll eine Liste
von Listen mit Schülernamen sein. Weiterhins soll beim Einlesen der Datei
auch die globale Variable `alle_schueler` befüllt werden. In `alle_schueler` 
sollen in einer Liste alle Schüler aufgelistet sein.

2. Schreibe eine Methode `haben_gemeinsamen_kurs` die zwei Schülernamen
als Parameter übergeben bekommt und als Rückgabewert `True` zurückliefert,
wenn beide Schüler einen gemeinsamen Kurs besuchen, ansonsten soll die
Methode `False` zurückgeben.

3. Schreibe eine Methode `hat_mit_allen_einen_gemeinsamen_kurs`, die einen
Schülernamen übergeben bekommt und genau dann `True` zurückliefert, wenn
der Schüler mit allen andren Schülern einen gemeinsamen Kurs besucht.
