#Beatriz Paulino - 21/03/25

#EX04

def categorias(idade):
    if idade >= 5 and idade <= 7:
        return "Infantil A"
    elif idade >= 8 and idade <= 10:
        return "Infatil B"
    elif idade >= 11 and idade <= 13:
        return "Juvenil A"
    elif idade >= 14 and idade <= 17:
        return "Juvenil B"
    elif idade >= 18:
        return "Sênior"

id = int(input())
cat = categorias(id)
print(cat)
    
