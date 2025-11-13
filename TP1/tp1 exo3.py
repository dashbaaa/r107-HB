jour = 3
heure = 10
minutes = 25

minutes_ecoulees = (jour-1) * 24 * 60 + heure * 60  + minutes
print(f"Depuis le début du mois, il s'est écoulé {minutes_ecoulees} minutes.")


our = int(input("Jour du mois (1..31) : "))
heure = int(input("Heure (0..23) : "))
minute = int(input("Minute (0..59) : "))
