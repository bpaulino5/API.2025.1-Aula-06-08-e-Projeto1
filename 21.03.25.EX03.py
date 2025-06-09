#Beatriz Paulino - 21/03/25

#EX03

def temp(cel):
    f = cel * (9.0/5.0) + 32.0
    return f

c = float(input())
tempe = temp(c)
print(tempe,"F")
