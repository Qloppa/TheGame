import time
import random
import numpy as np
from tkinter import *

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

#"""-----------------------------------GUI---------------------------------------#

root = Tk()
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack()

Label1 = Label(topFrame, text="THE GAME")
Label1.pack()

testList = [3234, 234, 434234, 234234, 23424333, 2342342, 442626]

varValue = len(testList)

Label2 = Label(topFrame, text=f"Du hälst jetzt " + str(varValue) + " Karten in deiner Hand.")
Label2.pack()
Quit = Button(bottomFrame, text="Beenden", command=root.destroy)
Quit.pack()
root.mainloop()

#"""-----------------------------------GUI---------------------------------------#

class Spielkarte:
  def __init__(self, value):
    self.value = value

  def getValue(self):
    return self.value

class Kartenstapel:

  spielKarten = []
  spK = np.arange(1,11, 1).tolist() #spK = Spielkarten // Erstellt eine Liste der Zahlen 1 - 100
  #print(spK)

  for spK0 in spK:
    spielKarten.append(Spielkarte(spK0))

  #spielKarten = [Spielkarte(1), Spielkarte(2), Spielkarte(3), Spielkarte(4), Spielkarte(5)] --ALT--
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
  time.sleep(1.5)
  print(spielKarte.getValue())

print("Handkarten:")

HandKarten = HandKarten()
HandKarten.nimmHandKarten(7)


for karte in HandKarten.handKarten:
  time.sleep(1.5)
  print(karte.getValue())

print("Kartenstapel:")

for spielKarte in Kartenstapel.spielKarten:
  time.sleep(1.5)
  print(spielKarte.getValue())
  
print("der Stapel ist leer")
