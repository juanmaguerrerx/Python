x = [1,2,3,4,5,6]

def sum(n):
    suma = 0
    for i in range(0,len(x)):
        suma += x[i]
    return suma
print(sum(x))