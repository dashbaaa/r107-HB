jour = int(input("Entrez le jour du mois (1..31) : "))
heure = int(input("Entrez l'heure (0..23) : "))
minute = int(input("Entrez les minutes (0..59) : "))

minutes_ecoulees = (jour - 1) * 24 * 60 + heure * 60 + minute

print(f"Depuis le début du mois, il s'est écoulé {minutes_ecoulees} minutes.")
