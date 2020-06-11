import time
import random

class Spielkarte:
  def __init__(self, value):
    self.value = value

  def getValue(self):
    return self.value

class Kartenstapel:
  
  spielKarten = [Spielkarte(1), Spielkarte(2), Spielkarte(3), Spielkarte(4), Spielkarte(5)]
  random.shuffle(spielKarten)

  def __init__(self):
    print("Kartenstapel initialisiert")

 
print("The Game:")

print("Kartenstapel:")

for spielKarte in Kartenstapel.spielKarten:
  time.sleep(1.5)
  print(spielKarte.getValue())
  
print("der Stapel ist leer")
