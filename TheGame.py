import time
import random
import numpy as np

class Spielkarte:
  def __init__(self, value):
    self.value = value

  def getValue(self):
    return self.value

class Kartenstapel:

  spielKarten = []
  spK = np.arange(1,101, 1).tolist() #spK = Spielkarten // Erstellt eine Liste der Zahlen 1 - 100
  #print(spK)

  for spK0 in spK:
    spielKarten.append(Spielkarte(spK0))

  #spielKarten = [Spielkarte(1), Spielkarte(2), Spielkarte(3), Spielkarte(4), Spielkarte(5)] --ALT--
  random.shuffle(spielKarten)


  def __init__(self):
    print("Kartenstapel initialisiert")

print("The Game:")

print("Kartenstapel:")

for spielKarte in Kartenstapel.spielKarten:
  time.sleep(1.5)
  print(spielKarte.getValue())
  
print("der Stapel ist leer")
