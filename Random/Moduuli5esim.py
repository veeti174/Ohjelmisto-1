"""
nimet = ["Viiv", "Ahmed", "Pekka", "Olga", "Mary"]

print(nimet[3])
print(nimet[1])
print(nimet[-2])
print(nimet[1:3])
print(nimet[2:])
print(nimet)

# Kysytään käyttäjältä nimet ja lisätään ne listaan
# Muokataan listan sisältöä.
"""

# luon tyhjän lista nimiä varten
nimet = []

# kysyn käyttäjältä osallistujen lukumäärän
lkm = int(input("Kuinka monta osallistujaa? ") )

# toistetaan nimien kysyminen
for i in range(lkm):
    nimi = input("Anna nimi: ")
    # lisätään saatu nimi listan loppuun (append)
    nimet.append(nimi)

# järjestetään nimet aakkosjärjestykseen.
nimet.sort()

print("Nimet aakkosjärjestykset")
print(nimet)

# muokataan listan alkioiden sisältöä
nimet[1] = "Toka"
nimet[-1] = "vika"
nimet.insert(index:0, object:"uusi eka")

# tulostetaan listan alkiot kukin omalla rivillään (for.. in)
for alkio in nimet:  # muuttujan nimen (nyt. alkio) vapaaehtoinen
    print(alkio)

