import os
import sys

def affiche(dossier):
    """Affiche le contenu du dossier passé en argument."""
    print(f"Contenu du dossier {dossier} :")
    for element in os.listdir(dossier):
        print(element)


def aide():
    """Affiche le message d'aide expliquant l'utilisation du script."""
    print("Erreur d'utilisation du script find1.py")
    print("Vous devez ajouter un nom de répertoire par exemple :")
    print("   python find1.py C:\\temp")


def main():

    if len(sys.argv) != 2:
        aide()
        return

    dossier = sys.argv[1]


    if not os.path.exists(dossier):
        print(f"Le répertoire {dossier} n'existe pas")
        aide()
        return


    if not os.path.isdir(dossier):
        print(f"{dossier} n'est pas un dossier")
        aide()
        return


    affiche(dossier)


if __name__ == "__main__":
    main()
