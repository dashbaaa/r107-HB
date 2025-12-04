notes = []
coeffs = []

print("Veuillez entrer les notes et coefficients des 5 modules.")
print("Format : note coeff (exemple : 10.5 2)")

for i in range(1, 6):
    saisie = input(f"Note du module {i} et coefficient : ")
    valeur = saisie.split()

note = float(valeur[0])
coeff = int(valeur[1])

notes.append(note)
coeffs.append(coeff)


somme = 0
somme_coeffs = 0

for i in range(5):
    somme += notes[i] * coeffs[i]
    somme_coeffs += coeffs[i]

moyenne = somme / somme_coeffs

print(f"\nMoyenne générale : {moyenne:.2f}")


admis = (moyenne >= 10) and all(note >= 8 for note in notes)

if admis:
    print("L'étudiant est ADMIS.")
else:
    print("L'étudiant n'est PAS admis.")