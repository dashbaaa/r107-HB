import random
mystere = random.randint(0, 100)
tentatives = 0

print("J'ai choisi un nombre entre 0 et 100. À toi de deviner !")

val = -1
while val != mystere:
    val = int(input("Votre proposition : "))
    tentatives += 1

if val < mystere:
    print("C'est plus grand.")
    elif val > mystere:(
        print("C'est plus petit."))
    else:
    print("Bravo, trouvé !")

print("Nombre de tentatives :", tentatives)