
print("\n--- Exercice 3 ---\n")


def ajouter_elt(lst=[0, 1, 2], elt=3):
    print("Appel -> id(lst) =", id(lst))
    lst.append(elt)
    return lst



print("a) Premier appel de ajouter_elt() :")
print(ajouter_elt())



print("\nb) Appels répétés de ajouter_elt() :")
print(ajouter_elt())
print(ajouter_elt())
print(ajouter_elt())



def ajouter_carac(ch="abc", elt="d"):
    print("Appel -> id(ch) =", id(ch))
    return ch + elt



print("\nd) Premier appel de ajouter_carac() :")
print(ajouter_carac())



print("\ne) Appels répétés de ajouter_carac() :")
print(ajouter_carac())
print(ajouter_carac())
print(ajouter_carac())
