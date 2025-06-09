#Beatriz Paulino
#11/04/25
#EX04

def soma_n(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

def main():
    n = int(input("Número: "))
    resultado = soma_n(n)
    print(resultado)
main()
