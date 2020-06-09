import time
import random

class Spielkarte:
  def __init__(self, value):
    self.value = value

  def getValue(self):
    return self.value

#A = Spielkarte(137)
#print(A.getValue())

print("The Game:")

print("Kartenstapel:")
stapelGroesse = 5
while stapelGroesse >0:
  print(random.randrange(0, 101, 2))
  time.sleep(1.5)
  stapelGroesse -= 1

print("der Stapel ist leer")
