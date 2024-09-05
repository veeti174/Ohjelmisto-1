import random
arvo=0
maks = int(input("Anna arvo: "))
def noppa(nums):
    total = 0
    heitto = "Nopan arvo"
    for num in nums:
        total += num
        print(heitto)
    return total
while arvo < 1:
    noppa1 = random.randint(1,maks)
    print(noppa([noppa1]))
    if noppa1 == maks:
        arvo +=1