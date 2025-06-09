#Beatriz Paulino
#11.04.25
#EX05

def eh_primo(n):
    if n <= 1:
        return False
    for i in range (2, n):
        if n % i == 0:
            return False
    return True

def numero():
    N = int(input("Digite un número: "))
    return N

n = numero()
print(eh_primo(n))
