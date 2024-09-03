"""
#print([1,5,3].sort())

# Funktio-esimerkkejä

def do_something():
    print("This aliohjelma tekee!")
    print("Jotakin hassua!")
    # return ei ole välttämätön ilmam sitä paluuarvo on None
    return "This is funktion palauttama merkkijono"

#return_value = do_something()
#print(return_value)

# Funktio, jolla parametreja (argumentteja)
# parametri muuttuja on käytössä vain funktion sisällä
def say_hello(to):
    #print("Moi " + to)
    return "Moi " + to

say_hello("Matti") # "Moi Matti"
print(say_hello("Matti"))

# useampi parametri, ja useampi arvo palautetaan listana
def create_greetings(to, count):
    greetings = []
    for i in range(1, count+1):
        #print(f"{i}, kerran Moi " + to)
        greetings.append(f"{i}, kerran Moi " + to)
    return greetings

greetings = create_greetings("Jorma", 3)
print(greetings)
# listan kaikkien arvojen käsittelu for-silmukalla, 2 tapaa
for i in range(len(greetings)):
    print(greetings[i])
for greetings in greetings:
    print(greetings)

# komentorivikäyttöliittymä

def hurraa_app():
    hooray_count = int(input("Kuinka monta kertaa hurrataan? "))
    hooray_counter = 0
    while hooray_counter < hooray_count:  # ehdosta syntyy aina True tai false
        # tulostetaan ehdosta syntyvä arvo
        # print(hooray_counter <3)
        hooray_counter = hooray_counter + 1
        print(hooray_counter < 3)
        print(f"{hooray_counter}, kerran Hurraa!")
    print(f"Hurrattiin {hooray_counter} kertaa")

def noppa_game():
    die1 = die2 = counter = 0
    while die1 != 6 or die2 != 6:
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        counter += 1
        # print(f"Nopan silmäluku: {die1}, heittojen lkm: {counter}")
    total_throw_count = total_throw_count + counter

command = ""
while command != "lopeta":
    command = input("Anna komento> ")
    if command == "tulosta":
        print("Tulostetaan")
    elif command == "lopeta":
        print("Lopetetaan ohjelma")
    elif command == "hurraa":
        hurraa_app
    elif command == "noppa":
        noppa_game

        #break # toistorakenteen suoritus loppuu heti
    else:
        print("En ymmärrä, Tarkista komentosi, kiitos.")
print("Ohlejman suoritus loppui.")

# globaali muuttuja (MAtti ei suosittele käyttöä)

main_app_var = 5
def modify_value():
    # muutetaan pääohjelman muuttujan arvoa
    global main_app_var
    main_app_var= 1
modify_value()
print(main_app_var)

"""

# Funktiot ja lista parametrina
#inventory muuttuujaan tallennetaan VIITTAUS olemassaolevaan
"""
def print_inventory(inventory):
    print("Pelaajalla on:")
    for item in inventory:
        print(item)
    inventory.append("uusi juttu lisätty funktion sisällä")

player1_inventory = ["veitsi", "vesipullo"]
player2_inventory = ["kirves", "eväsleipä"]

print_inventory(player1_inventory)
print_inventory(player2_inventory)
# tulostus muuttuu, koska funktion muokkasi samaa listaa
print_inventory(player1_inventory)
print_inventory(player2_inventory)


# sama stringi-arvolla: alkupeäsiten muuttujien arvo ei muutu
def print_inventory_str(inventory):
    print("Pelaajalla on: " + inventory)
    inventory += ", uusi juttu lisätty funktion sisällä"

player1_inventory = "veitsi, vesipullo"
player2_inventory = "kirves, eväsleipä"

print_inventory_str(player1_inventory)
print_inventory_str(player2_inventory)
# tulostus ei muutu
print_inventory_str(player1_inventory)
print_inventory_str(player2_inventory)
"""

# nimetyt parametrit ja oletusarvot

def calc_sum(num1=0, num2=0, num3=0):
    print(f"Laskutoimitus: {num1} + {num2} + {num3}")
    return num1 + num2 + num3
print(calc_sum(2))
print(calc_sum(2, num3=5))
print(calc_sum(1, 4, 6))

# vaihtuvanmittainen argumenttijono
# *numd -> nums muuttujaan muodostuu lista parametreista
def calc_sum_adv(nums):
    total = 0
    calculation = "Laskutoimitus:"
    for num in nums:
        total += num
        calculation = calculation + " +" + str(num)

        print(calculation)
    return total

print(calc_sum_adv([1, 2, 3, 6]))
