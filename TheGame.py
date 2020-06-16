import time
import random
import numpy as np
from tkinter import *

TG_Version = "0.0.1"

def loadList(filename):
    # Die Dateiendung sollte .npy sein [Numpy]
    tempNumpyArray=np.load(filename)
    return tempNumpyArray.tolist()

def safeList(myList, filename):
    np.save(filename, myList)

def getRev():
    rev_old = loadList("rev_old_file.npy")  # Lädt die alte Revisionsnummer
    rev_old
    e = int(rev_old[0])
    c = e + 1
    rev_new = int(c)
    rev_old = [rev_new]
    print(f"Version: " + TG_Version + "(Rev." + str(rev_old[0]) + ")")
    safeList(rev_old, "rev_old_file") #Speichert die Revisionsnummer

def doNothing():
    print("OK, I do Nothing")

getRev() # Ersetzt die alte gegen die neue Revisionsnummer und gibt diese aus.





""" 

- GUI Section -
Das GUI werde ich hier oben machen soll das dann nachher in diesem File bleiben oder
machen wir das in ein anderes? 

Das Modul was ich nehme wird erstmal TKinter sein. Gibt viele Videos darüber bei Youtube.
Gibt aber auch noch alternativen die vielleicht noch besser sind aber erst mal für Hauptmenü oder
eine minimale Spieloberfläche wie bei Solitär oder Hearts da muss man grafisch dann noch nicht so
viel umsetzen! 



UM DAS GUI RAUSZUNEHMEN EINFACH RAUTEN AM ANFANG DER ZEILE ENTFERNEN!
↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
"""

# """-----------------------------------GUI---------------------------------------#
root = Tk()
root.title("THE GAME!")
root.iconbitmap("THE_GAME_ICON.ico")

def aboutTG():
    newWindow = Toplevel(root)
    newWindow.title("Über The Game")
    newWindow.iconbitmap("THE_GAME_ICON.ico")
    newWindow.geometry("250x30")
    Label1 = Label(newWindow, text="The Game\n" +
                   "by Qloppa & Balboran")
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

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack()

Label1 = Label(topFrame, text="THE GAME")
Label1.pack()

listHandkarten = []
Quit = Button(bottomFrame, text="Beenden", command=root.destroy)
Quit.pack()


# """-----------------------------------GUI---------------------------------------#
class Spielkarte:
    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value


class Kartenstapel:
    spielKarten = []
    spK = np.arange(1, 11, 1).tolist()  # spK = Spielkarten // Erstellt eine Liste der Zahlen 1 - 100
    # print(spK)

    for spK0 in spK:
        spielKarten.append(Spielkarte(spK0))

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
