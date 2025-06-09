#Beatriz Paulino
#11.04.25
#EX07

def inverter_numero(n):
    n_invertido = str(n)[::-1]
    if n < 0:
        return -int(n_invertido[:-1])
    return int(n_invertido)

n = int(input("Digite um número: "))
print(inverter_numero(n))
