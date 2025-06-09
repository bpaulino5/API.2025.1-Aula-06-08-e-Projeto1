#Beatriz Paulino
#11/04/25
#EX03

def soma_n(n):
    s = 0
    for i in range(1, n+1):
        s += i
    return s

def main():
    n = int(input("Número: "))
    resultado = soma_n(n)
    print(resultado)
main()
