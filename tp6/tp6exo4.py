import random


def generer(nbr, vmin, vmax):
    table = []
    for _ in range(nbr):
        table.append(random.randint(vmin, vmax))
    return table

def combienInferieur(table, vseuil):
    compteur = 0
    for valeur in table:
        if valeur < vseuil:
            compteur += 1
    return compteur


nb = 100
print(f"Générer {nb} nombres entiers entre 0 et 100")

tab = generer(nb, 0, 100)
tab.sort()

print(tab)

total = combienInferieur(tab, 25)
print(f"Il y en a {total} inférieurs à 25")



print("\n--- VERSION INTERACTIVE ---")


nb = int(input("Combien de valeurs voulez-vous générer ? "))


vmin = int(input("Valeur minimale ? "))
vmax = int(input("Valeur maximale ? "))


reponse = input("Vous voulez préciser le seuil ? (Oui/O/Non/N) : ")

if reponse.lower() in ("oui", "o"):
    vseuil = int(input("Donnez la valeur du seuil : "))
else:
    vseuil = 30
    print("Seuil par défaut appliqué : 30")


tab = generer(nb, vmin, vmax)
tab.sort()

print("\nTableau généré :")
print(tab)


total = combienInferieur(tab, vseuil)

print(f"\nIl y en a {total} inférieurs à {vseuil}")
