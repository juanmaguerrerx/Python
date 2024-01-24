# The same but stop the loop if a number is not greater that its predecessor.

numbers = [7, 8, 12, 29, 75, 150, 180, 145, 525, 50]

for x in range(0,len(numbers)):
    if numbers[x] % 4 == 0 or numbers[x] % 5 == 0:
        if numbers[x] > numbers[x-1]:
            print(numbers[x])