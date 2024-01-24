x = [2,3,1,4,5,6]

def smallest(n): 
    num=n[0]
    for i in range(1,len(n)):
        if n[i] < num:
            num = n[i]
    return num
print(smallest(x))