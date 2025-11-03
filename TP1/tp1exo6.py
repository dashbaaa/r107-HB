
minutes = int(input("Entrez le nombre de minutes écoulées depuis le début du mois : "))

#Calcul du jour, de l'heure et des minutes
jour = minutes // (24 * 60) + 1
reste = minutes % (24 * 60)
heure = reste // 60
minute = reste % 60

#affichage du résultat
print(f"\nDate correspondante : Jour {jour}, {heure}h{minute:02d}")
