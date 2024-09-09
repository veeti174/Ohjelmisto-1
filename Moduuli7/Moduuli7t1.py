kuukaudet = ("Talvi", "Talvi", "Kevät", "Kevät", "Kevät", "Kesä", "Kesä", "Kesä", "Syksy", "Syksy", "Syksy", "Talvi")
luku = int(input("Give me a months number (1-12): "))
kuukausi = kuukaudet[luku-1]
print(f"{luku}. vuoden aika on {kuukausi}")