class listas:

    def __init__(self,x):
        self.x = x
    def __init__(self,n):
        self.n = n
    
    def sum(x):
        num = 0
        for i in range(0,len(x)):
            num += x[i]
        return num
    
    def max(n): 
        num=n[0]
        for i in range(1,len(n)):
            if n[i] > num:
                num = n[i]
        return num
    
    def min(n):
        num=n[0]
        for i in range(1,len(n)):
            if n[i] < num[i-1]:
                num = n[i]
        return num
    
    def avg(x):
        sum = 0
        for i in range(0,len(x)):
            sum += x[i]
        return sum
    

