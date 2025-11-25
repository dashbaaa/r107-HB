
login1 = input("Login du premier etudiant : ")
login2 = input("Login du second etudiant : ")

binome = (login1, login2)

print(f"L'etudiant {binome[0]} est en binome avec l'etudiant {binome[1]}")


nouveau_login = input("Nouveau login pour changer de binome : ")

print("\nTentative de modification du second element du tuplet...")
try:
binome[1] = nouveau_login # ceci provoque normalement une erreur
except TypeError as e:
print("Impossible de modifier un tuplet (tuple immuable) :", e)


print("\nTentative de suppression du second element du tuplet...")
try:
del binome[1]
except TypeError as e:
print("Impossible de supprimer un element d'un tuplet :", e)


login3 = input("\nLogin du troisieme etudiant pour former un trinome : ")

trinome = binome + (login3,)
print("Trinome forme :", trinome)

print("\nConclusion : les tuplets sont immuables, on ne peut ni les modifier ni "
"supprimer un element ; pour les 'modifier', on en cree un nouveau.")