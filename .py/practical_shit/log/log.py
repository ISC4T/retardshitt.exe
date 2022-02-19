import time
def loginScript():
    userLogin = False
    signOrSetup = input("Sign in, Sign up: ")

    def signIn(): # Sign in
        user = input("Username? ")
        userPass = (input("Password? "))

        with open('userDB.txt') as file: # Checks the login credentials
            if ((user + "\n") + userPass) in file.read():
                userLogin = True

    def signUp(): # Sign Up
        user = input("Username? ")
        userPass = (input("Password? "))

        with open('userDB.txt') as file:
            if (user) in file.read(): # Checks if Username exists
                print("Username Already exists")
            else:
                with open("userDB.txt", "r") as file: # Pusts (Username + Password) in userDB.txt
                    userDB_file = file.readlines()
            
                userDB_file.append(((user + "\n") + userPass) + "\n")

                with open("userDB.txt", "a") as userDB:
                    contents = "".join(userDB_file)
                    userDB.write(contents)

                loopsignin = input("Sign In(Y, N)? ") # Asks if you want to sign in
                if loopsignin.lower() == ("y"):
                    signIn()
                    if userLogin == True:
                        print("Success!")
                    else:
                        print("Login Failed")
                        print("Try Again")
                        time.sleep(1)
                        signIn()

    # Start and Confirm Sign up
    if signOrSetup.lower() == ("sign up"):
        signUp()

    # Start and Confirm Sign in
    if signOrSetup.lower() == ("sign in"):
        signIn()
        if userLogin == True:
            print("Success!")
        else:
            print("Login Failed")
            print("Try Again")
            time.sleep(1)
            signIn()
            
if __name__ == "__main__":
    loginScript()