
import random


nb = random.randint(0, 100)

print(f"Nombre généré : {nb}")


if nb < 50:
print("Pile !")
else:
print("Face !")