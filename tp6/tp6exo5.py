import unicodedata



def enlever_accents(texte):

    texte = unicodedata.normalize('NFD', texte)

    texte_sans_accents = ''.join(
        c for c in texte if unicodedata.category(c) != 'Mn'
    )
    return texte_sans_accents



def nettoyer(texte):
    texte = texte.lower()
    texte = enlever_accents(texte)


    resultat = ''.join(c for c in texte if c.isalpha())
    return resultat



def est_palindrome(texte):
    return texte == texte[::-1]



def main():
    chaine = input("Entrez un mot ou une phrase : ")

    propre = nettoyer(chaine)

    if est_palindrome(propre):
        print("C'est un palindrome !")
    else:
        print("Ce n'est pas un palindrome.")


main()
