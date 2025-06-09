#Beatriz Paulino
#11/04/25

#EX01

def par_ou_impar(n):
    if n%2 == 0:
        return 'par'
    else:
        return 'impar'

def main():
    n = int(input("Número: "))
    resultado = par_ou_impar(n)
    print(f'O número é {resultado}')
    
main()
