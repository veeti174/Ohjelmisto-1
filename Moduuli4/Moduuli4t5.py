user = ""
sala = ""
python = 1
rules = 2
rounds = 0
while rounds < 5:
    while user != python or sala != rules:
        rounds = rounds + 1
        user = input("Username input here.: ")
        sala = input("Password input here.: ")
        if user == python:
            print("Username correct. ")
            sala = input("Password input here.: ")
            if sala == rules:
                print("Password correct")
            if user == python and sala == rules:
                print("Tervetuloa")
            else:
                print("Wrong username or password")
        else:
            print("Wrong username or password")