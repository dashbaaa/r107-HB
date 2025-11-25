
firstname = input("Votre prenom : ")
name = input("Votre nom : ")
promo = input("Votre promo : ")
group = input("Votre groupe de TP : ")

dic = {
"firstname": firstname,
"name": name,
"promo": promo,
"group": group
}

print(f"votre nom est '{dic['name']}', prenom est '{dic['firstname']}', "
f"vous faites partie de la promo '{dic['promo']}' et votre groupe est '{dic['group']}'")


print("\nLes cles du dictionnaire sont :")
for k in dic.keys():
print(f"-{k}")

print("Les valeurs du dictionnaire sont :")
for v in dic.values():
print(f"-{v}")

print("Les tuplets du dictionnaire sont :")
for item in dic.items():
print(f"-{item}")


print("\n===== Deuxieme personne =====")
firstname2 = input("Prenom 2 : ")
name2 = input("Nom 2 : ")
promo2 = input("Promo 2 : ")
group2 = input("Groupe 2 : ")

dic2 = {
"firstname": firstname2,
"name": name2,
"promo": promo2,
"group": group2
}


print("\n===== Creation du dictionnaire binome =====")
id1 = input("Identifiant (id) pour le premier etudiant : ")
id2 = input("Identifiant (id) pour le second etudiant : ")

binome = {
id1: dic,
id2: dic2
}


print("\nLes etudiants formants le binome sont :")
for etu in binome.values():
    print(f"- L'etudiant {etu['name']} {etu['firstname']} du groupe {etu['group']}")