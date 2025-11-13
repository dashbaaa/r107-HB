n = int(input("Saisir un entier positif : "))

choix = input("Choisir la boucle (for / while) : ")


fact = 1


if choix == "for":
    for i in range(1, n + 1):
        fact *= i
        print("Étape", i, ": fact =", fact)

elif choix == "while":
    i = 1
    while i <= n:
        fact *= i
        print("Étape", i, ": fact =", fact)
        i += 1

else:
    print("Choix invalide.")

print("Factorielle de", n, "=", fact)