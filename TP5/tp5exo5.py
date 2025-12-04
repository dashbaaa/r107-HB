heures = float(input("Nombre d'heures travaillées : "))
taux = float(input("Salaire horaire (en euros) : "))

salaire = 0.0

if heures <= 160:
    salaire = heures * taux
elif heures <= 200:
    salaire = 160 * taux \
              + (heures - 160) * taux * 1.25
else:
    alaire = 160 * taux \
             + 40 * taux * 1.25 \
             + (heures - 200) * taux * 1.5

print(f"Salaire brut : {salaire:.2f} euros")