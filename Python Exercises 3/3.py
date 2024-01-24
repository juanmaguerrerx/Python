#Python exercises 3

# Write some functions that take a tuple of integers as
# argument and return the following:

#1. The sum of the elements

def f1(mytuple):
  mysum = 0
  for x in mytuple:
    mysum += x
  return mysum

y = (3, 8, 4, 5, 6, 7)
print(f1(y))
print(sum(y))

#2. The smallest element.

def f2(mytuple):
  mymin = mytuple[0]
  for i in range(1,len(mytuple)):
    if mytuple[i] < mymin:
      mymin = mytuple[i]
  return mymin

y = (3, 8, 4, 5, 6, 7)
print(f2(y))
print(min(y))

#3. The largest element.

def f3(mytuple):
  mymax = mytuple[0]
  for i in range(1,len(mytuple)):
    if mytuple[i] > mymax:
      mymax = mytuple[i]
  return mymax

y = (3, 8, 4, 5, 6, 7)
print(f3(y))
print(max(y))

#4. How many elements are multiple of the number passed as second argument.

def f4(mytuple, mydiv):
  c = 0
  for x in mytuple:
    if x % mydiv == 0:
      c += 1
  return c

y = (3, 8, 4, 5, 6, 7)
print(f4(y, 3))

#5. An object with sum, count, avg, max and min from the elements.

class myclass:
  su = 0
  co = 0
  av = 0.0
  ma = 0
  mi = 0
  
def f5(mytuple):
  myobject = myclass()
  myobject.su = sum(mytuple)
  myobject.co = len(mytuple)
  myobject.av = sum(mytuple) / len(mytuple)
  myobject.ma = max(mytuple)
  myobject.mi = min(mytuple)
  return myobject

y = (3, 8, 4, 5, 6, 7)
z = myclass()
z = f5(y)
print("Sum:",z.su)
print("Count:",z.co)
print("Avg:",z.av)
print("Max:",z.ma)
print("Min:",z.mi)

#6. Nothing, but order the tuple and eliminate duplicates.
#  This is impossible, only lists can be passed by reference as arguments

def f6(mytuple):
  t = list(mytuple)
  t.sort()
  i = 0
  while i < len(t)-1:
    if t[i] == t[i+1]:
      t.pop(i)
    else:
      i += 1
  mytuple = tuple(t)
  print(mytuple)
  
x = (3, 3, 3, 8, 4, 5, 4, 4, 4, 6, 7, 8, 8, 8, 1, 1)
f6(x)
print(x)

#7. Nothing, but reverse the tuple

#8. A copy of the tuple ordered and without duplicates.
# Don’t change the original tuple.

def f8(mytuple):
  t = list(mytuple)
  t.sort()
  i = 0
  while i < len(t)-1:
    if t[i] == t[i+1]:
      t.pop(i)
    else:
      i += 1
  return tuple(t)
  
x = (3, 3, 3, 8, 4, 5, 4, 4, 4, 6, 7, 8, 8, 8, 1, 1)
print(f8(x))
print(x)

#9. True if all the tuple elements are the same, 
#otherwise return false.

def f9(mytuple):
  for i in range(1,len(mytuple)):
    if mytuple[0] != mytuple[i]:
      return False
  return True
  
x = (3, 3, 3, 3, 3, 3)
y = (3, 3, 4, 3, 3, 3)
print(f9(x))
print(f9(y))

# 10. True if all the tuple elements are greater 
# than the number passed as second parameter

def f10(mytuple, y):
  for x in mytuple:
    if x <= y:
      return False
  return True
  
z = (3, 3, 3, 8, 4, 5, 4, 4, 4, 6, 7, 8, 8, 8, 1, 1)
print(f10(z,0))
print(f10(z,1))
