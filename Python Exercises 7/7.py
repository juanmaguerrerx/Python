d = dict()
mifile = input("File name:")
f = open(mifile,"rt")
s = f.read()

print("1. The whole string:")
print(s)

print("\n2. The string, one character per line:")
for c in s:
    print(c)

print("\n3. The number of repetitions for each character:")
for c in s:
    if c in d:
        d.update({c: d.get(c) + 1})
    else:
        d.update({c: 1})
print(d)

print("\n4. Keys unordered:")
print(d.keys())

print("\n5. Keys ordered:")
print(sorted(d.keys()))

print("\n6. Keys in descending order:")
print(sorted(d.keys(), reverse=True))

print("\n7. Values unordered:")
print(d.values())

print("\n8. Values ordered:")
print(sorted(d.values()))

print("\n9. Values in descending order:")
print(sorted(d.values(), reverse=True))

print("\n10. Items unordered:")
print(d.items())

print("\n11. Items ordered by key:")
print(sorted(d.items(), key=lambda x: x[0]))
print(sorted(d.items()))

print("\n12. Items in descending order by key:")
print(sorted(d.items(), key=lambda x: x[0], reverse=True))
print(sorted(d.items(), reverse=True))

print("\n13. Items ordered by value:")
print(sorted(d.items(), key=lambda x: x[1]))

print("\n14. Items in descending order by value:")
print(sorted(d.items(), key=lambda x: x[1], reverse=True))