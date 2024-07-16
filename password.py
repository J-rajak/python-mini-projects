pwd = ("input enter the master password")

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            print(line,rstrip())
            
def add():
    name = input("account name: ")
    pwd = input("password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + " " + pwd + "\n")

while True:

    mode = input("would you like to add a new password or view previous ones").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    if mode == "add":
        add()
    else:
        print("invalid mode")
        continue
