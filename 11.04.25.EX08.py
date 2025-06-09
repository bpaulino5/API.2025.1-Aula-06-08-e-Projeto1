#Beatriz Paulino
#11.04.25
#EX08

def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

n = int(input("Digite um número: "))
print(fibonacci(n))
