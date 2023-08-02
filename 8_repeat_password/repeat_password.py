password = input("Password: ")

while True:
    passwordR = input("Repeat password: ")
    if password == passwordR:
        break
    print("They do not match!")
print("User account created!")