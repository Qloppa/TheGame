import time

print("Hello World")

felixstinks = True
fs = 2
while felixstinks:
  print("Felix müffelt")
  time.sleep(0.5)
  fs = fs*2
  print(fs)

  if fs >= 100:
    felixstinks = False
else:
  print("Tut er trotzdem!")
