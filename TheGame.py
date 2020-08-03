import random
import numpy as np
from VersionControl import VersionControl
from Model import Kartenstapel, Handkarten, Spielkarte, Spieler, AblageStapelBereich, AblageStapel
import View

TG_Version = "0.0.5"
Final = True

stapelGroesse = 99

spielerListe = []

spieler1 = Spieler("Felix")
spielerListe.append(spieler1)

KS = Kartenstapel(stapelGroesse)
print(list(map(lambda x: x.getValue(), KS.spielKarten)))

print(f"Handkarten von {spieler1.name}:")
spieler1.zieheHandKarten(7, KS)

VC = VersionControl(TG_Version)

abgelegteKarte = Spielkarte(0)

ablageStapelBereich = AblageStapelBereich()

if Final == False:  # DEAKTIVIERT DAS ZÄHLEN DER REVISIONEN IM FINALEN BUILD
    VC.getRev()
else:
    VC.releaseRev()

# """-----------------------------------GUI---------------------------------------#

View.init(TG_Version, VC.useRev())


def buttonPressed(event):
    value = View.getClickedValue()
    print(f"karte geklickt: {value}")
    View.setClickedValue(0)

    if value > 0:
        print(f"value: {value}")
        global abgelegteKarte
        abgelegteKarte = spieler1.karteAblegen(value)
        print(f"abgelegteKarte: {abgelegteKarte.value}")
        View.deleteHandkarten()
        View.setClickedValue(0)
        for karte in spieler1.handKarten.handKarten:
            View.handKarteAnzeigen(karte)
    if value < 0:
        View.deleteAblagestapel()
        ablageStapelBereich.updateAblageStapel(value + 4, abgelegteKarte)
        View.aktualisiereAblageStapel(ablageStapelBereich.ablageStapel)


root = View.createWindow()

#print(f"Spielername: {View.player1name}")
print("geht los")
View.createImage()
View.aktualisiereAblageStapel(ablageStapelBereich.ablageStapel)
root.bind("<Button-1>", buttonPressed)
View.createButtons()
root.update()
# """-----------------------------------GUI---------------------------------------#

print("The Game:")

print("Kartenstapel:")

for karte in spieler1.handKarten.handKarten:
    View.handKarteAnzeigen(karte)

print(list(map(lambda x: x.getValue(), spieler1.handKarten.handKarten)))

# ablegeKarte = input("welche Karte willst du spielen? ")

# spieler1.karteAblegen(View.getClickedValue())

print(list(map(lambda x: x.getValue(), spieler1.handKarten.handKarten)))

print("Kartenstapel:")

print(list(map(lambda x: x.getValue(), KS.spielKarten)))

root.mainloop()