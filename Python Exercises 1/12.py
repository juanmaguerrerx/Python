numbers = [7, 8, 12, 29, 75, 150, 180, 145, 525, 50]

for x in range(0,len(numbers)):
    if numbers[x] % 4 == 0 or numbers[x] % 5 == 0:
        print(numbers[x])

    