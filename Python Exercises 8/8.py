import string
import os.path
d = dict()
mifile = input("File name: ")
if not os.path.isfile(mifile):
    print("Error: file",mifile,"does not exist")
    exit()
f = open(mifile,"rt")
s = f.read()
print("The string:")
print(s)
s = s.translate(str.maketrans('', '', string.punctuation))
s = s.lower()
mylist = s.split()
for w in mylist:
    if w in d:
        d.update({w: d.get(w) + 1})
    else:
        d.update({w: 1})
print("The number of repetitions for each word:")
print(sorted(d.items()))