

nombre = float(input("Vous cherchez la table de multiplication de quel nombre ?\n"))

resultats = []
for i in range(10):
    produit = nombre * i
    resultats.append(produit)
    for i in range(10):
        print(f"{nombre} * {i} = {round(resultats[i], 1)}")