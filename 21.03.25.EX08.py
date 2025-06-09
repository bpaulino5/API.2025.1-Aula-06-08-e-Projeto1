#Beatriz Paulino - 21/03/25

#EX08

def calcular(n1, n2, n3):
    m = (n1 + n2 + n3) / 3
    if m >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

nn1 = float(input("N1:"))
nn2 = float(input("N2:"))
nn3 = float(input("N3:"))

med = calcular(nn1, nn2, nn3)
print(med)
