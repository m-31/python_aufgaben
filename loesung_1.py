alle_schüler = []
kurse = []

def ordnen(dateiname):
    global kurse
    global alle_schüler
    alle_schüler = []
    kurse = []
    with open(dateiname, 'r') as f:
        for x in f.readlines():

            zeile = x.strip()
            y = zeile.split(' ')
            alle_schüler = alle_schüler + y

            kurse.append(y)
def haben_gemeensamen_kurs(x, y):
    for kurs in kurse:
        if x in kurs and y in kurs:
            return True
    return False



ordnen('pythagoras.txt')

alle_schüler = list(set(alle_schüler))
print(alle_schüler)
print(haben_gemeensamen_kurs("Anton", "Petra"))
print(haben_gemeensamen_kurs("Anton", "Tim"))