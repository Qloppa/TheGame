import random
import numpy as np
from VersionControl import VersionControl
from Model import Kartenstapel, Handkarten, Spielkarte, Spieler, AblageStapelBereich, AblageStapel
from View import SampleApp, GameFrame

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
app = SampleApp()

#

try:
    
    app.init(TG_Version, VC.useRev())


    def buttonPressed(event):
        value = app.getClickedValue()
        print(f"karte geklickt: {value}")
        app.setClickedValue(0)

        if value > 0:
            print(f"value: {value}")
            global abgelegteKarte
            abgelegteKarte = spieler1.karteAblegen(value)
            print(f"abgelegteKarte: {abgelegteKarte.value}")
            app.deleteHandkarten()
            app.setClickedValue(0)
            for karte in spieler1.handKarten.handKarten:
                app.handKarteAnzeigen(karte)
        if value < 0:
            app.deleteAblagestapel()
            ablageStapelBereich.updateAblageStapel(value + 4, abgelegteKarte)
            app.aktualisiereAblageStapel(ablageStapelBereich.ablageStapel)


    #root = theGame.createWindow()

    #print(f"Spielername: {View.player1name}")
    print("geht los")
    #theGame.createImage()
    app.aktualisiereAblageStapel(ablageStapelBereich.ablageStapel)
    #root.bind("<Button-1>", buttonPressed)
    app.createButtons()
    #root.update()



    print("The Game:")

    print("Kartenstapel:")

    for karte in spieler1.handKarten.handKarten:
        app.handKarteAnzeigen(karte)

    print(list(map(lambda x: x.getValue(), spieler1.handKarten.handKarten)))

    # ablegeKarte = input("welche Karte willst du spielen? ")

    # spieler1.karteAblegen(View.getClickedValue())

    print(list(map(lambda x: x.getValue(), spieler1.handKarten.handKarten)))

    print("Kartenstapel:")

    print(list(map(lambda x: x.getValue(), KS.spielKarten)))

except:
    pass

app.mainloop()