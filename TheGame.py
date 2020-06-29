import random
import numpy as np
from VersionControl import VersionControl
from Model import Kartenstapel, Handkarten, Spielkarte, Spieler
import View
from tkinter import *
import tkinter as tk
from PIL import ImageTk
from PIL import Image

TG_Version = "0.0.4"
Final = False

VC = VersionControl(TG_Version)

stapelGroesse = 99

if Final == False: #DEAKTIVIERT DAS ZÄHLEN DER REVISIONEN IM FINALEN BUILD
    VC.getRev()
else:
    VC.releaseRev()

# """-----------------------------------GUI---------------------------------------#

root = View.createWindow()
#View.aboutTG(TG_Version, str(VC.useRev))
View.createImage()
View.createButtons()

# """-----------------------------------GUI---------------------------------------#

print("The Game:")

spielerListe = []

spieler1 = Spieler("Felix")
spielerListe.append(spieler1)

print("Kartenstapel:")

KS = Kartenstapel(stapelGroesse)
print(list(map(lambda x: x.getValue(), KS.spielKarten)))

print(f"Handkarten von {spieler1.name}:")
spieler1.zieheHandKarten(7, KS)

for karte in spieler1.handKarten.handKarten:
    View.generate(karte)
print(list(map(lambda x: x.getValue(), spieler1.handKarten.handKarten)))

print("Kartenstapel:")

print(list(map(lambda x: x.getValue(), KS.spielKarten)))

"""
textLabel = Label(topFrame, text=f"Du hälst jetzt " + str(
    len(spieler1.handKarten.handKarten)) + " Karten in deiner Hand.\n" + "Es sind die Zahlen: " + str(list(map(lambda x: x.getValue(), spieler1.handKarten.handKarten))))
textLabel.pack()
"""

root.mainloop()