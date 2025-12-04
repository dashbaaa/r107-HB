
nom1 = input("Nom de la première personne : ")
prenom1 = input("Prénom de la première personne : ")

nom2 = input("Nom de la deuxième personne : ")
prenom2 = input("Prénom de la deuxième personne : ")


nom1_formate = nom1.strip().upper()
prenom1_formate = prenom1.strip().capitalize()

nom2_formate = nom2.strip().upper()
prenom2_formate = prenom2.strip().capitalize()


personnes = [
(nom1_formate, prenom1_formate, f"{prenom1_formate} {nom1_formate}"),
(nom2_formate, prenom2_formate, f"{prenom2_formate} {nom2_formate}")
]


personnes_triees = sorted(personnes, key=lambda p: (p[0], p[1]))


for nom affichage in personnes_triees:
print(affichage)

