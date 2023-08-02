attempts = 0

while True:
    pin = input("PIN: ")
    if pin == "4321":
        attempts += 1
        break
    else:
        attempts += 1
        print("Wrong")

if attempts == 1:
    print("Correct! It only took you one single attempt!")
else:
    print(f"Correct! It took you {attempts} attempts")