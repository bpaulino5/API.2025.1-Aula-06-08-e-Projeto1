def media_ponderada (nota1, nota2, nota3):
    media = ((nota1 * 2) + (nota2 * 3) + (nota3 * 5)) / 10
    return media

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))

if media_ponderada(nota1, nota2, nota3) >= 6:
    print("Aprovado")
else:
    print("Reprovado")
