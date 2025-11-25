
L = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7]


valeur_max = L[0]
freq_max = 0

for i in range(len(L)):
    valeur = L[i]
    freq = 0

for j in range(len(L)):
    if L[j] == valeur:
        freq += 1

if freq > freq_max:
    freq_max = freq
    valeur_max = valeur
    print(f"Le nombre le plus frequent dans la liste est le : {valeur_max} ({freq_max} x)")

L = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7]

valeur_max = L[0]
freq_max = L.count(L[0])

for elt in L:
    freq = L.count(elt)
if freq > freq_max:
    freq_max = freq
    valeur_max = elt
    print(f"Le nombre le plus frequent dans la liste est le : {valeur_max} ({freq_max} x)")

