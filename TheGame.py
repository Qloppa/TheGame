import random
import numpy as np
from VersionControl import VersionControl
from Model import Kartenstapel, Handkarten, Spielkarte, Spieler
import View

TG_Version = "0.0.4"
Final = False

stapelGroesse = 99

spielerListe = []

spieler1 = Spieler("Felix")
spielerListe.append(spieler1)

KS = Kartenstapel(stapelGroesse)
print(list(map(lambda x: x.getValue(), KS.spielKarten)))

print(f"Handkarten von {spieler1.name}:")
spieler1.zieheHandKarten(7, KS)

VC = VersionControl(TG_Version)



if Final == False: #DEAKTIVIERT DAS ZÄHLEN DER REVISIONEN IM FINALEN BUILD
    VC.getRev()
else:
    VC.releaseRev()

# """-----------------------------------GUI---------------------------------------#

View.init(TG_Version, VC.useRev())

def buttonPressed(event):
    print("karte geklickt")
    value = View.getClickedValue()
    if value > 0:
        spieler1.karteAblegen(value)
        print(f"value: {value}")
        View.deleteHandkarten()
        View.setClickedValue(0)
        for karte in spieler1.handKarten.handKarten:
            View.karteAnzeigen(karte)
    if value == -4:
        print("hat geklappt")

root = View.createWindow()
root.bind("<Button-1>", buttonPressed)
View.createImage()
View.createButtons()

# """-----------------------------------GUI---------------------------------------#

print("The Game:")

print("Kartenstapel:")

for karte in spieler1.handKarten.handKarten:    
    View.karteAnzeigen(karte)
    

print(list(map(lambda x: x.getValue(), spieler1.handKarten.handKarten)))

#ablegeKarte = input("welche Karte willst du spielen? ")

#spieler1.karteAblegen(View.getClickedValue())

print(list(map(lambda x: x.getValue(), spieler1.handKarten.handKarten)))

print("Kartenstapel:")

print(list(map(lambda x: x.getValue(), KS.spielKarten)))

root.mainloop()