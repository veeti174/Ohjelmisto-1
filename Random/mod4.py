# sisäkkäiset silmukat

eka = 1
while eka <= 5:
    print("Ulompi silmukka alkaa")
    toka = 1
    while toka <= 5:
        print("Sisempi silmukka alkaa")
        print(f"{eka} kertaa {toka} on {eka*toka}")
        toka = toka +1
    eka = eka +1