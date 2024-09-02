luvut = []

luku = input("May I have your number?: ")
if luku != "":
    luvut.append(luku)
    luvut.sort()
while luku != "":
    luku = input("May i have your number?: ")
    if luku == "":
        break
    luvut.append(luku)
    luvut.sort()


print(luvut[-1])
print(luvut[-2])
print(luvut[-3])
print(luvut[-4])
print(luvut[-5])
