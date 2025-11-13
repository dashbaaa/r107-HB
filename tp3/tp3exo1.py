N = int(input("a) entrer N : "))
somme = sum(range(N + 1))
print("Somme =", somme)


val = 0
while val != 100:
    val = int(input("b) entrer une valeur (100 pour arrêter) : "))
    print("Terminé.")


inf10 = entre10et15 = sup15 = 0

for i in range(10):
    v = int(input("c) Valeur (0-20) : "))
    while not(0 <= v <= 20):
        v = int(input("Recommence (0-20) : "))
        if v < 10:
            inf10 += 1
            elif v < 15:
            entre10et15 += 1
            else:
            sup15 += 1

print("<10 :", inf10)
print("10-15 :", entre10et15)
print(">=15 :", sup15)


X = int(input("d) entrer X : "))
s, n = 0, 0

while s <= X:
    s += n
    n += 1

print("N trouvé :", n - 1)
print("Somme =", s)