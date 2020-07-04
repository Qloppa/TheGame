import random

class Spielkarte:

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

class Kartenstapel:

    def __init__(self, size):
        print("Kartenstapel initialisiert")
        self.size = size
        self.spielKarten = []
        self.stapelErzeugen()

    def stapelErzeugen(self):
        for i in range(2, self.size):
            self.spielKarten.append(Spielkarte(i))
        random.shuffle(self.spielKarten)   

class Handkarten:

    def __init__(self):
        print("HandKarten initialisiert")
        self.handKarten = []

class AblageStapel:
    
    def __init__(self, spielKarte):
        self.spielKarte = spielKarte

class AblageStapelBereich:

    def __init__(self):
        self.ablageStapel = [Spielkarte(1),Spielkarte(3),Spielkarte(3),Spielkarte(7)]

    def updateAblageStapel(self, index, spielKarte):
        self.ablageStapel[index] = spielKarte

class Spieler:

    def __init__(self, name): #Konstruktor zur initialisierung der Klasse
        self.handKarten = Handkarten() #eigenes Handkartenobjekt
        self.name = name
    
    def zieheHandKarten(self, anzahl, kartenstapel):
        for _ in range(anzahl):
            self.handKarten.handKarten.append(kartenstapel.spielKarten.pop())

    def karteAblegen(self, nummer):
            for spielKarte in self.handKarten.handKarten:
                while n == False:
                    if spielKarte.getValue()==nummer:
                        self.handKarten.handKarten.remove(spielKarte)
                    else:
                        n