nMax = 10 # ou 3 comme indiqué dans le sujet
v1 = []
v2 = []


n = int(input(f"Quelle est la taille de vos vecteurs [entre 1 et {nMax}] ? "))

while n < 1 or n > nMax:
    print("Taille incorrecte.")
    n = int(input(f"Quelle est la taille de vos vecteurs [entre 1 et {nMax}] ? "))

print("Saisie du premier vecteur :")
for i in range(n):
    val = float(input(f"v1[{i}] = "))
    v1.append(val)

print("Saisie du second vecteur :")
for i in range(n):
    val = float(input(f"v2[{i}] = "))
    v2.append(val)


produit_scalaire = 0.0
for i in range(n):
    produit_scalaire += v1[i] * v2[i]
    print(f"Le produit scalaire de v1 par v2 vaut {produit_scalaire}")

