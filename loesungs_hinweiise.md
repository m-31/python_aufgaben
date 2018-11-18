# Allgemeine Lösungshinsweise

## Erstelle Testdatensätze

Am besten erstellst du dir weitere Datensätze, mit denen du dein Program später testen kannst.
Dazu gehören ganz einfache Fälle, Negativbeispiele, etc.
Für Aufgabe 1 sind das zum Beispiel die folgenden Dateien:
[aufgabe_1_1.txt](aufgabe_1_1.txt), [aufgabe_1_2.txt](aufgabe_1_2.txt), 
[aufgabe_1_3.txt](aufgabe_1_3.txt), [aufgabe_1_4.txt](aufgabe_1_4.txt).
Überlege dir vorher dazu das erwartete Ergebnis.


## Bennene deine Methoden sprechend

Du solltest dein Program in kurze Methoden aufteilen, die für bestimmte Teilaufgaben
zuständig sind. Benenne die Methoden so, dass jeder sofort versteht, was die Methode
macht. Schreibe gegebnenfalls auch einen Kommentar über die Methode, die weitere
Erklärungen zu der Methode, ihren Eingabewerten und ggf. ihren Ausgabewerten enthält

Vergesse nicht, dass globale Variablen, die in der Methode verändert werden sollen,
am Anfang der Methode aufgelistet werden müssen. Z.B.:

    # Einlesen aller Kurse aus einer Datei
    #   schreibt die Daten in die globalen Variablen 'kurse' und 'alle_schueler'
    def datei_lesen(dateiname):
        global alle_schueler, kurse



## Baue eine eine *debug* Methode ein 

Am Anfang deines Programmes solltest du eine  `debug` Methode einbauen.
Gib dann in deinem Programm an verschiedenen Stellen interessante Zwischenergebnisse
aus, damit du im Fehlerfalle den Ablauf einfach nachvollziehen kannst.

    test = True

    def debug(message):
        if test:
            print('>> ' + str(message))

Wenn alles läuft, kannst du durch Setzen von  `debug = False` die Ausgabe dieser
Hilfsnachrichten wieder ausschalten. Wenn dann wieder ein Fehler auftritt und du
*debuggen* musst, kannst du die Ausgabe wieder einschalten.


## Teste in deinem Programm die Testdatensätze

In deinem Programm lässt du die Hauptroutine auch mit den Testdatensätzen laufen und
kontrollierst das Ergebnis mit der `assert` Methode:

        assert(['Lilli'] == finde_alle('aufgabe_1_1.txt'))

Wenn du dein Programm entwickelst kannst du dir dann immer sicher sein, dass auch nach
Änderungen noch alles richtig funktioniert.

 