chaine = input("Entrez un mot ou une phrase : ")


chaine = chaine.lower()


lettres = ""
for c in chaine:
    if c.isalpha():
        lettres += c


if lettres == lettres[::-1]:
    print("C'est un palindrome !")
else:
    print("Ce n'est pas un palindrome.")