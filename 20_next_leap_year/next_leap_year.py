year = int(input('Year: '))
yearN = year

while True: 
    year += 1
    if year % 100 == 0:
        if year % 400 == 0:
            break
    elif year % 4 == 0:
        break

print(f"The next leap year after {yearN} is {year}")  