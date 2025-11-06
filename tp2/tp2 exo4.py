
BASE = 4

fromage = 800.0

eau = 2.0

ail = 2.0


pain = 400.0


nbConvives = int(input("Entrez le nombre de personne(s) conviées à la fondue : "))


nouveauFromage = fromage * nbConvives / BASE
nouvelleEau = eau * nbConvives / BASE
nouvelAil = ail * nbConvives / BASE
nouveauPain = pain * nbConvives / BASE


print(f"\nPour faire une fondue fribourgeoise pour {nbConvives} personnes, il vous faut :")
print(f"- {nouveauFromage:.1f} gr de fromage")
print(f"- {nouvelleEau:.1f} dl d'eau")
print(f"- {nouvelAil:.1f} gousse(s) d'ail")
print(f"- {nouveauPain:.1f} gr de pain")