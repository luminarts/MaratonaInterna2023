n, m = [int(i) for i in input().split()]


map=[]

for i in range(n):
    aux = [i for i in input().split()]
    map.append(aux)
    
for i in range(m):
    print(map[i])

