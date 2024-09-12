"""
airports = ()
while True:
    kysy = input("What do want? Search for aiport = 1 Input new airport = 2 Lopeta or stop = x: ")
    kysy = kysy.lower()
    if kysy == "x":
        break
    elif kysy == "1":
        ICAO = input("Anna ICAO koodi: ")
        ICAO = ICAO.upper()
        for i in airports:
            if i[0] == ICAO:
                print(i[1])
                break
        else:
            print("Unknown input")
    elif kysy == "2":
        airport = input("Syötä lentokentän nimi: ")
        ICAO = input("Syötä lentokentän icao koodi: ")
        airport.capitalize()
        ICAO = ICAO.upper()
        i = [ICAO, airport]
        airports.append(i)
    else:
        print("Unknown input")
"""
airports = []
while True:
    kysy = input("What do want? Search for aiport = 1 Input new airport = 2 Lopeta or stop = x: ")
    kysy = kysy.lower()
    if kysy == "x":
        break
    elif kysy == "2":
        airport = input("Syötä lentokentän nimi: ")
        ICAO = input("Syötä lentokentän icao koodi: ")
        airport.capitalize()
        ICAO = ICAO.upper()
        i = [ICAO, airport]
        airports.append(i)
    elif kysy == "1":
        ICAO = input("Anna ICAO koodi: ")
        ICAO = ICAO.upper()
        for i in airports:
            if i[0] == ICAO:
                print(i[1])
                break
        else:
            print("Unknown input")
    else:
        print("Unknown input")