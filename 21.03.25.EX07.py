#Beatriz Paulino - 21/03/25

#EX07

def multiplo(n):
    if n %3 == 0 or n %5 == 0:
        return True
    else:
        return False

nn = int(input())
resul = multiplo(nn)
print(resul)
