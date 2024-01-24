x = [1,2,3,4,5,6,7,8]
y = int(input("Type a number: "))

def multiplos(lista, numero):
    multiplo = []
    for i in range(0,len(lista)):
        if numero % lista[i] == 0:
            multiplo.append(lista[i])
    return multiplo


print("Los multiplos de ",y," son: ",multiplos(x,y))