L1 = [0] * 3
print(L1, type(L1), id(L1))

for elem in L1:
    print(elem, type(elem), id(elem))

L1[1] += 1
print(L1, type(L1), id(L1))

for elem in L1:
    print(elem, id(elem))

chaine = "machine"

for c in chaine:
    print(c, type(c), id(c))
