#Beatriz Paulino - 21/03/25

#EX05

def lados(l1, l2, l3):
    if l1 + l2 > l3 and l3 + l2 > l1:
        if l1 == l2 and l1 == l3:
            return "Triângulo equilátero"
        elif l1 == l2 or l2 == l3 or l1 == l3:
            return "Triângulo isóceles"
        elif l1 != l2 and l2 != l3:
            return "Triângulo escaleno"

lado1 = int(input("Lado 1"))
lado2 = int(input("Lado 2"))
lado3 = int(input("Lado 3"))

if lado1 > 0 and lado2 > 0 and lado3 > 0:
    resul = lados(lado1, lado2, lado3)
    print(resul)
