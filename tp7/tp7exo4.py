import os
import sys

def recherche(dossier, fichier):
    """
    Recherche dans 'dossier' et ses sous-dossiers :
    - tous les dossiers (listeDossiers)
    - tous les fichiers portant le nom 'fichier' (listeFichiers)
    """

    listeDossiers = []
    listeFichiers = []


    if not dossier.endswith(os.sep):
        dossier = dossier + os.sep

    a_explorer = [dossier]

    while a_explorer:
        d = a_explorer.pop()

        try:
            contenu = os.listdir(d)
        except PermissionError:
            print(f"Accès refusé : {d}")
            continue

        for elt in contenu:
            chemin = os.path.join(d, elt)


            if os.path.isfile(chemin):
                if elt == fichier:
                    listeFichiers.append(chemin)


            elif os.path.isdir(chemin):
                listeDossiers.append(chemin)
                a_explorer.append(chemin + os.sep)



    return listeFichiers, listeDossiers


def aide():
    print("Usage : python find.py -d <dossier> -f <fichier>")
    print("Exemple : python find.py -d C:\\temp -f toto.txt")


def main():

    if "-d" not in sys.argv or "-f" not in sys.argv:
        aide()
        return

    try:
        dossier = sys.argv[sys.argv.index("-d") + 1]
        fichier = sys.argv[sys.argv.index("-f") + 1]
    except Exception:
        aide()
        return


    if not os.path.exists(dossier):
        print("Le dossier indiqué n'existe pas.")
        return

    if not os.path.isdir(dossier):
        print("L'argument fourni avec -d n'est pas un dossier.")
        return


    listeFichiers, listeDossiers = recherche(dossier, fichier)


    for f in listeFichiers:
        print(f)


if __name__ == "__main__":
    main()
