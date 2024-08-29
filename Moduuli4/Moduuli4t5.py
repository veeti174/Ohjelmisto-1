user = ""
sala = ""
python = 1
rules = 2
rounds = 0
while user != python or sala != rules or rounds < 5:
    while rounds < 5:
        rounds += 1
        user = input("Username input here.: ")
        if user == "python":
            print("Username correct. ")
            sala = input("Password input here.: ")
            if sala == "rules":
                print("Tervetuloa")
            else:
                print("Wrong username or password")
        if sala != user:
            input("Paasword input here.: ")
            print("Wrong username or password")
    else:
        print("Pääsy evätty")
        break