import time
import random
print("The Game:")

print("Kartenstapel:")
stapelGroesse = 5
while stapelGroesse >0:
  print(random.randrange(0, 101, 2))
  time.sleep(1.5)
  stapelGroesse -= 1

print("der Stapel ist leer")
