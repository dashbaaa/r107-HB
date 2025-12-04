def taille(T):
    compteur = 0
 for c in T:
    compteur += 1
    return compteur

def pourcentage_voyelles(T):
    voyelles = "aeiouyAEIOUY"
    nb_voy = 0
    nb_alpha = 0

for c in T:
    if c.isalpha():
        nb_alpha += 1
        if c in voyelles:
            nb_voy += 1

if nb_alpha == 0:
    return 0
    return (nb_voy / nb_alpha) * 100




T = input("Entrez une phrase : ")

print("Taille de la chaîne :", taille(T))
print("Pourcentage de voyelles : {:.2f}%".format(pourcentage_voyelles(T)))

pos = trouver_wwagon(T)
if pos != -1:
    print(f'Le mot "wagon" apparaît à la position {pos}.')
else:
    print('Le mot "wagon" n\'apparaît pas.')

print("Nombre total d'occurrences de 'wagon' :", compter_wagon(T))

