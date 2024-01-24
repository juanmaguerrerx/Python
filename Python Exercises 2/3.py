x = [2,3,1,14,5,6]

def largest(n): 
    num=n[0]
    for i in range(1,len(n)):
        if n[i] > num:
            num = n[i]
    return num
print(largest(x))