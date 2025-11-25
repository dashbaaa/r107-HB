date_str = input("Entrez une date au format jjmmaaaa : ")

if len(date_str) != 8 or not date_str.isdigit():
    print("Format incorrect, veuillez saisir une date au format jjmmaaaa.")
else:
    jour = int(date_str[0:2])
    mois = int(date_str[2:4])
    annee = int(date_str[4:8])


def est_bissextile(a):
    return (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0)


jours_par_mois = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if est_bissextile(annee):
    jours_par_mois[1] = 29 # février = index 1


date_valide = True

if mois < 1 or mois > 12:
    date_valide = False
else:
    max_jour = jours_par_mois[mois - 1]
    if jour < 1 or jour > max_jour:
        date_valide = False
if date_valide:
    print("Date correcte.")
else:
    print("Date incorrecte.")