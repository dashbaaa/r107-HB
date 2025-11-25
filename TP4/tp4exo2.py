
nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0

notes = []
for i in range(nombreEtudiants):
    while True:
        note = float(input(f"Note etudiant {i} : "))
        if 0.0 <= note <= 20.0:
            break
        else:
            print("Erreur : la note doit être comprise entre 0 et 20.")
            notes.append(note)
            moyenne += note


moyenne = moyenne / nombreEtudiants

print(f"Moyenne de classe : {moyenne}")

print("Numero de l'Etudiant | note | ecart a la moyenne")
for i in range(nombreEtudiants):
    ecart = notes[i] - moyenne
    print(f"{i} | {notes[i]} | {ecart}")