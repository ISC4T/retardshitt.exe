signOrSetup = input("Sign in, Sign up: ")

def signIn():
    user = input("Username? ")
    userPass = (input("Password? "))

    with open('userDB.txt') as file:
     if (user + userPass) in file.read():
         userLogin = True

def signUp():
    user = input("Username? ")
    userPass = (input("Password? "))
    with open("userDB.txt", "r") as file:
        userDB_file = file.readlines()
        
    userDB_file.append((user + userPass) + "\n")

    with open("userDB.txt", "a") as userDB:
	    contents = "".join(userDB_file)
	    userDB.write(contents)

    loopsignin = input("Sign In(Y, N)? ")
    if loopsignin.lower() == ("y"):
        signIn()

if signOrSetup.lower() == ("sign up"):
    signUp()

if signOrSetup.lower() == ("sign in"):
    signIn()
    if  == True:
        print("Success!")