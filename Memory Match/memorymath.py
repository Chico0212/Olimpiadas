def is_in(c, p, car):
    if car.get(c) is None:
        car[c] = {p}
    else:
        car[c].add(p)

cartas = dict()
k = int(input())
n = int(input())

pares_possiveis = k/2

for i in range(n):
    p1, p2, c1, c2 = input().split()
    if c1 != c2:
        is_in(c1, p1, cartas)
        is_in(c2, p2, cartas)
    else:
        if c1 in cartas:
            cartas.pop(c1)
        pares_possiveis -= 1

cont = 0
for carta in cartas:
    if len(cartas[carta]) == 2:
        cont +=1

if len(cartas) == pares_possiveis:
    cont = pares_possiveis
elif pares_possiveis - cont == 1:
    cont = 1
elif pares_possiveis < k/2 and len(cartas) > 0:
    cont = int(pares_possiveis)

print(cont)