import time
import random
import numpy as np
from tkinter import *
import tkinter as tk
from PIL import ImageTk
from PIL import Image
TG_Version = "0.0.2"
Final = False

#testcomment

def loadList(filename):
    # Die Dateiendung sollte .npy sein [Numpy]
    tempNumpyArray=np.load(filename)
    return tempNumpyArray.tolist()

def safeList(myList, filename):
    np.save(filename, myList)

if Final == False: #DEAKTIVIERT DAS ZÄHLEN DER REVISIONEN IM FINALEN BUILD
    def getRev():
        rev_old = loadList("rev_old_file.npy")  # Lädt die alte Revisionsnummer
        e = int(rev_old[0])
        c = e + 1
        rev_new = str(c)
        rev_old = [rev_new]
        print(f"Version " + TG_Version + "(Rev." + rev_new + ")")
        safeList(rev_old, "rev_old_file") #Speichert die Revisionsnummer
else:
    rev_old = loadList("rev_old_file.npy")  # Lädt die alte Revisionsnummer
    e = int(rev_old[0])
    c = e
    rev_new = str(c)
    rev_old = [rev_new]
    if Final == True:
        TG_Version = "(Release): " + TG_Version
    def getRev():
        pass
    print(f"Version " + TG_Version + "(Rev." + rev_new + ")")


def useRev():
    rev_old = loadList("rev_old_file.npy")   # Lädt die alte Revisionsnummer
    return rev_old[0]

def doNothing():
    print("OK, I do Nothing")

getRev() # Ersetzt die alte gegen die neue Revisionsnummer und gibt diese aus.

""" - GUI Section -

Das GUI werde ich hier oben machen soll das dann nachher in diesem File bleiben oder
machen wir das in ein anderes? 

Das Modul was ich nehme wird erstmal TKinter sein. Gibt viele Videos darüber bei Youtube.
Gibt aber auch noch alternativen die vielleicht noch besser sind aber erst mal für Hauptmenü oder
eine minimale Spieloberfläche wie bei Solitär oder Hearts da muss man grafisch dann noch nicht so
viel umsetzen! 



UM DAS GUI RAUSZUNEHMEN EINFACH RAUTEN AM ANFANG DER ZEILE ENTFERNEN!
↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓"""

# """-----------------------------------GUI---------------------------------------#
root = Tk()
root.title("THE GAME!")
root.iconbitmap("THE_GAME_ICON.ico")
root.geometry("1920x1080")

# """-----------------------------------MENU---------------------------------------#

def aboutTG():
    newWindow = Toplevel(root)
    newWindow.title("Über The Game")
    newWindow.iconbitmap("THE_GAME_ICON.ico")
    newWindow.geometry("250x60")
    Label1 = Label(newWindow, text=f"The Game\n" +
                   "by Qloppa & Balboran\n" +
                   "Ver. " + TG_Version + "." + str(useRev()))
    Label1.pack()

menu = Menu(root)
subMenu = Menu(menu)
root.config(menu=menu)

menu.add_cascade(label="Spiel", menu=subMenu)
subMenu.add_command(label="Neues Spiel", command=doNothing)
subMenu.add_command(label='Über The Game', command=aboutTG)
subMenu.add_separator()
subMenu.add_command(label="Beenden", command=root.destroy)

editMenu = Menu(menu)
menu.add_cascade(label="Einstellungen", menu=editMenu)
editMenu.add_command(label="1337", command=doNothing)

# """-----------------------------------IMAGE---------------------------------------#
scale = 0.60

w = int(439*scale)
h = int(638*scale)

backgroundImage = Image.open("./Kartengrafiken/Spielkarte_MUSTER_0.png")
backgroundImage = backgroundImage.resize((w,h), Image.ANTIALIAS)
background = ImageTk.PhotoImage(backgroundImage)

upImage = Image.open("./Kartengrafiken/Spielkarte_MUSTER_ARROW_UP.png")
upImage = upImage.resize((w,h), Image.ANTIALIAS)
up = ImageTk.PhotoImage(upImage)

downImage = Image.open("./Kartengrafiken/Spielkarte_MUSTER_ARROW_Down.png")
downImage = downImage.resize((w,h), Image.ANTIALIAS)
down = ImageTk.PhotoImage(downImage)

ablagestapelFrame = Frame(root)
ablagestapelFrame.pack(side=TOP)

ablageKarte = Frame(ablagestapelFrame)
ablageKarte.pack(side = LEFT)

canvas1_1 = tk.Canvas(ablageKarte, width=w, height=h)
canvas1_1.pack(side='top', fill=None, expand=False)

canvas1_1.create_image(0,0, image=up, anchor=NW)

canvas1_1.create_text(w/2, 60*scale, text="99", font="Chiller 42", fill="white", anchor=CENTER) #mitt oben
canvas1_1.create_text(w/2, h-100*scale, text="1", font="Chiller 125", fill="white", anchor=CENTER) #mitte unten

ablageKarte = Frame(ablagestapelFrame)
ablageKarte.pack(side = LEFT)

canvas1_2 = tk.Canvas(ablageKarte, width=w, height=h)
canvas1_2.pack(side='top', fill=None, expand=False)

canvas1_2.create_image(0,0, image=up, anchor=NW)

canvas1_2.create_text(w/2, 60*scale, text="99", font="Chiller 42", fill="white", anchor=CENTER) #mitt oben
canvas1_2.create_text(w/2, h-100*scale, text="1", font="Chiller 125", fill="white", anchor=CENTER) #mitte unten

ablageKarte = Frame(ablagestapelFrame)
ablageKarte.pack(side = LEFT)

canvas100_1 = tk.Canvas(ablageKarte, width=w, height=h)
canvas100_1.pack(side='top', fill=None, expand=False)

canvas100_1.create_image(0,0, image=down, anchor=NW)

canvas100_1.create_text(w/2, 125*scale, text="100", font="Chiller 110", fill="white", anchor=CENTER) #mitt oben
canvas100_1.create_text(w/2, h-50*scale, text="2", font="Chiller 50", fill="white", anchor=CENTER) #mitte unten

ablageKarte = Frame(ablagestapelFrame)
ablageKarte.pack(side = LEFT)

canvas100_2 = tk.Canvas(ablageKarte, width=w, height=h)
canvas100_2.pack(side='top', fill=None, expand=False)

canvas100_2.create_image(0,0, image=down, anchor=NW)

canvas100_2.create_text(w/2, 125*scale, text="100", font="Chiller 110", fill="white", anchor=CENTER) #mitt oben
canvas100_2.create_text(w/2, h-50*scale, text="2", font="Chiller 50", fill="white", anchor=CENTER) #mitte unten

handkartenFrame = Frame(root)
handkartenFrame.pack(side=BOTTOM)

# """-----------------------------------BUTTONS---------------------------------------#

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack()

title = Label(topFrame, text="THE GAME")
title.pack()

quit = Button(bottomFrame, text="Beenden", command=root.destroy)
quit.pack()


# """-----------------------------------GUI---------------------------------------#

class Spielkarte:
    def __init__(self, value, handkartenFrame):
        self.value = value
        self.handkartenFrame = handkartenFrame
    
    def generate(self):
        cardFrame = Frame(self.handkartenFrame)
        cardFrame.pack(side = LEFT)

        scale = 0.6

        w = 439*scale
        h = 638*scale

        canvas = tk.Canvas(cardFrame, width=w, height=h)
        canvas.pack(side='top', fill=None, expand=False)

        canvas.create_image(0,0, image=background, anchor=NW)

        canvas.create_text(30*scale, 20*scale, text=self.value, font="Chiller 42", fill="white", anchor=NW) #links oben
        canvas.create_text(w-20*scale, 20*scale, text=self.value, font="Chiller 42", fill="white", anchor=NE) #rechts oben
        canvas.create_text(30*scale, h, text=self.value, font="Chiller 42", fill="white", anchor=SW) #links unten
        canvas.create_text(w-20*scale, h, text=self.value, font="Chiller 42", fill="white", anchor=SE) #rechts unten
        canvas.create_text(w/2, h*0.6, text=self.value, font="Chiller 137", fill="white", anchor=CENTER) #mittlere Zahl

    def getValue(self):
        return self.value


class Kartenstapel:
    spielKarten = []
    spK = np.arange(1, 11, 1).tolist()  # spK = Spielkarten // Erstellt eine Liste der Zahlen 1 - 100
    # print(spK)

    for spK0 in spK:
        spielKarten.append(Spielkarte(spK0, handkartenFrame))

    # spielKarten = [Spielkarte(1), Spielkarte(2), Spielkarte(3), Spielkarte(4), Spielkarte(5)] --ALT--
    random.shuffle(spielKarten)

    def __init__(self):
        print("Kartenstapel initialisiert")


class HandKarten:
    handKarten = []

    def __init__(self):
        print("HandKarten initialisiert")

    def nimmHandKarten(self, anzahl):
        for x in range(anzahl):
            self.handKarten.append(Kartenstapel.spielKarten.pop())


print("The Game:")

print("Kartenstapel:")

for spielKarte in Kartenstapel.spielKarten:
    #time.sleep(0.5)
    print(spielKarte.getValue())

print("Handkarten:")

HandKarten = HandKarten()
HandKarten.nimmHandKarten(7)
listHandkarten = []

for karte in HandKarten.handKarten:
    #time.sleep(0.5)
    print(karte.getValue())
    karte.generate()
    listHandkarten.append(karte.getValue())
    print(listHandkarten)

print("Kartenstapel:")

for spielKarte in Kartenstapel.spielKarten:
    #time.sleep(0.5)
    print(spielKarte.getValue())

print("der Stapel ist leer")

Label2 = Label(topFrame, text=f"Du hälst jetzt " + str(
    len(listHandkarten)) + " Karten in deiner Hand.\n" + "Es sind die Zahlen: " + str(listHandkarten))
Label2.pack()

root.mainloop()
