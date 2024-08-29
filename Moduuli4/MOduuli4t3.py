
high=int(0)
low=int(0)

luku = input("May I have your number?: ")
if luku != "":
    high = int(luku)
    low = int(luku)
while luku != "":
    luku = input("May i have your number?: ")
    if luku == "":
        break
    luku = int(luku)
    if (luku < low):
        low = luku
    if (luku > high):
        high = luku

print(f"The lowest number you have is {low}.")
print(f"The highest number you have is {high}")