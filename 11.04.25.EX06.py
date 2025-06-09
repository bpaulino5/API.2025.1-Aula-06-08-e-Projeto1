#Beatriz Paulino
#11.04.25
#EX06

def maior_digito(n):
    n_str = str(n)
    maior = max(int(digit) for digit in n_str)
    return maior

n = int(input("Digite um número: "))
print(maior_digito(n))
