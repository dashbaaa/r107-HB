import os
from datetime import datetime


f1 = input("Nom du premier fichier : ")
f2 = input("Nom du deuxième fichier : ")


existe1 = os.path.isfile(f1)
existe2 = os.path.isfile(f2)

if not existe1:
    print(f"Le fichier '{f1}' n'existe pas.")
    if not existe2:

rint(f"Le fichier '{f2}' n'existe pas.")


if not (existe1 or existe2):
    print("Aucun des deux fichiers n'existe. Fin du programme.")
exit()


if existe1:
    taille1 = os.path.getsize(f1)
    print(f"Taille de '{f1}' : {taille1} octets")

if existe2:
    taille2 = os.path.getsize(f2)
    print(f"Taille de '{f2}' : {taille2} octets")



fichiers_existants = []
if existe1:
    fichiers_existants.append(f1)
    if existe2:
        fichiers_existants.append(f2)

fichier_recent = None
date_recent = None

for nom in fichiers_existants:
    t = os.path.getmtime(nom)
    if (date_recent is None) or (t > date_recent):
        date_recent = t
        fichier_recent = nom


date_lisible = datetime.fromtimestamp(date_recent)

print(f"\nLe fichier le plus récent est : '{fichier_recent}'")
print("Date de dernière modification :", date_lisible)