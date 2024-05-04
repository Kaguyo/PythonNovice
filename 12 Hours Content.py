#0
Monday, Tuesday, Chocolate = 1, 2, "DOCE"
Monday = str(Monday)
Tuesday = str(Tuesday)
print("Monday is"+" "+Monday+"st",
      "Tuesday is"+" "+Tuesday+"nd",
      Chocolate)
#1
import time

for ammo in range(30,0,-1):
    print(ammo)
    time.sleep(0.1)
print ("Out of ammo!")
#2
ammo = ""

while ammo == 0:
    ammo = input("Press "R" to reload!")

print("Lock and Loaded.")


