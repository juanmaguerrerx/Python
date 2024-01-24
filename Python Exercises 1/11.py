numUser = input("Escribe un numero: ")
numUser = int(numUser)

resultado = 0

for x in range(0,numUser):
    resultado+=x

print(f"La suma de los numeros entre el 0 y el {numUser} es: {resultado}")