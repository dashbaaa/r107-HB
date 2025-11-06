

nb = int(input("Entrez un nombre entier : "))


if nb > 0:
signe = "positif"
elif nb < 0:
signe = "négatif"
else:
signe = "zéro"


if nb == 0:
parite = "(et il est pair)" #cas special
elif nb % 2 == 0:
parite = "et pair"
else:
parite = "et impair"


print(f"Le nombre est {signe} {parite}")