#Beatriz Paulino - 21/03/25

#EX06

def calculadora(preco):
    if preco > 100:
        p = preco - (preco * 0.1)
        return p
    if preco <= 100:
        p = preco - (preco * 0.05)
        return p

pr = float(input())
resul = calculadora(pr)
print(resul)
