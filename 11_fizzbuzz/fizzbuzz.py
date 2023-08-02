num = int(input("Number: "))

x = num % 3
y = num % 5

if x == 0 and y != 0:
    print("Fizz")
elif y == 0 and x != 0:
    print("Buzz")
elif x == 0 and y == 0:
    print("FizzBuzz")