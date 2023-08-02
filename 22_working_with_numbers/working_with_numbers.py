count = 0
countP = 0
countN = 0
total_sum = 0

print("Please type in integer numbers. Type in 0 to finish.")
while True:
    num = int(input("Number: "))
    if num == 0:
        break
    elif num < 0:
        countN += 1
    else:
        countP += 1
    count += 1
    total_sum += num
mean = total_sum / count
print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {total_sum}")
print(f"The mean of the numbers is {mean}")
print(f"Positive numbers {countP}")
print(f"Negative numbers {countN}")