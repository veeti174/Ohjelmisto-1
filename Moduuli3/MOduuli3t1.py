
pituus = int( input("Kuinka pitkä on kuha sentteinä?: ") )

if (pituus >=37):
    # Tämä on ns if-ehdon  lohko (block)
    # Tänne tullaan, jos ehto on totta, eli
    # PItuus on suurempi tai yhtäsuuri kuin 37
    print("Mennään grillaamaan!")

else:
    erotus = 37-pituus
    print("Kuhan pitäisi olla " + str(erotus) + " cm pidempi")


