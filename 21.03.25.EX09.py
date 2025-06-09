#Beatriz Paulino - 21/03/25

#EX09
def bissexto(ano):
    if ano %4 == 0 and ano %100 == 0 and ano %400 == 0:
        return "Bissexto"
    elif ano %4 == 0 and ano %100 == 0 and ano %400 !=0:
        return "Não é bissexto"
    elif ano %4 == 0 and ano %100 != 0:
        return "Bissexto"
    elif ano %4 != 0:
        return "Não é bissexto"

n = int(input("Ano:"))
resul = bissexto(n)
print(resul)
