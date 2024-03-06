count = 0
sumNum = 0

while True:
    userNum = input("Escribe un numero: ")
    userNum = int(userNum)
    
    if userNum == 0:
        break
    
    sumNum += userNum
    count += 1

print(f"Total de números ingresados: {count}")
print(f"Suma de los números ingresados: {sumNum}")