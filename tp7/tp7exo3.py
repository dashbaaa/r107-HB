import os
import sys


def recherche(dossier):
    """Renvoie deux listes :
       - listeFichiers : chemins complets des fichiers
       - listeDossiers : chemins complets des dossiers
    """


    listeFichiers = []
    listeDossiers = []


    if not dossier.endswith(os.sep):
        dossier = dossier + os.sep


    a_explorer = [dossier]

    while a_explorer:
        dossier_courant = a_explorer.pop()

        try:
            contenu = os.listdir(dossier_courant)
        except PermissionError:
            print(f"Accès refusé : {dossier_courant}")
            continue

        for elt in contenu:
            chemin = dossier_courant + elt

            if os.path.isfile(chemin):
                listeFichiers.append(chemin)

            elif os.path.isdir(chemin):

                listeDossiers.append(chemin)
                a_explorer.append(chemin + os.sep)

            else:

                pass

    return listeFichiers, listeDossiers


def aide():
    print("Usage : python find2.py <nom_dossier>")
    print("Exemple : python find2.py C:\\temp")


def main():
    if len(sys.argv) != 2:
        aide()
        return

    dossier = sys.argv[1]

    if not os.path.exists(dossier):
        print("Le dossier indiqué n'existe pas.")
        aide()
        return

    if not os.path.isdir(dossier):
        print("L'argument fourni n'est pas un dossier.")
        aide()
        return

    fichiers, dossiers = recherche(dossier)

    print("\n--- LISTE DES DOSSIERS ---")
    for d in dossiers:
        print(d)

    print("\n--- LISTE DES FICHIERS ---")
    for f in fichiers:
        print(f)


if __name__ == "__main__":
    main()
