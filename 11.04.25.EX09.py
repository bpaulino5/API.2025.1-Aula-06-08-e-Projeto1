#Beatriz Paulino
#11.04.25
#EX09

def contagem_regressiva(n):
    for i in range(n, -1, -1):
        print(i)
    print('FIM!')

n = int(input("Digite um número: "))
contagem_regressiva(n)
