import random
noppa = ()
summa = (1)

lkm = int(input("Kuinka monta noppaa? ") )
for i in range(lkm):
    noppa = random.randint(1, 6)
    summa = summa + noppa
print(f"Noppien silmälukujen summa {summa}.")
# = random.randint(1 ,6)