
x = float(input("Entrez un nombre décimal : "))


appartient = (2 <= x <= 3) or (0 < x <= 1) or (-10 < x <= -2)
if appartient:
    print("x appartient à I")
else:
    print("x n'appartient pas à I")