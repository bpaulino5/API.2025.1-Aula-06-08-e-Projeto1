#Beatriz Paulino - 21/03/25

#EX02

def converter(h, m, s):
    ho = h * 3600
    mi = m * 60
    seg = ho + mi + s
    return seg

nh = int(input("digite h:"))
nm = int(input("digite m:"))
ns = int(input("digite s:"))

con = converter(nh, nm, ns)
print(f"{con}")
