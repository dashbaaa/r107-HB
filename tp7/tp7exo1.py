import sys

def main():

    nb_args = len(sys.argv)


    nom_script = sys.argv[0]


    if nb_args == 1:
        print(f"Pas assez d'arguments pour le script '{nom_script}'")
    else:
        print(f"Liste des arguments passés au script {nom_script} :")

        for arg in sys.argv[1:]:
            print(" ➜", arg)

if __name__ == "__main__":
    main()
