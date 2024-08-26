sukupuoli = input("Oletko nainen vai mies biologisesti? kirjoita N tai M ")
Hemo = int(input("Mitka ovat hemoglobiini arvosi? "))
if sukupuoli == "M":
    if Hemo > 195:
        print("Sinun Hemoglobiini arvosi ovat korkeat")
    elif Hemo >= 134:
        print ("Sinun hemoglobiini arvosi ovat normaalit.")
    elif Hemo <134:
        print("Sinun hemoglobiini arvosi ovat matalat.")
elif sukupuoli == "N":
    if Hemo > 175:
        print("Sinun Hemoglobiini arvosi ovat korkeat")
    elif Hemo >= 117:
        print("Sinun hemoglobiini arvosi ovat normaalit.")
    elif Hemo < 117:
        print("Sinun hemoglobiini arvosi ovat matalat.")