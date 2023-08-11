n, k =[int(i) for i in input().split()]

v = [int(i) for i in input().split()]

def avg(sales, interval_size, listofsales):
    aux = 0
    aux2 = 0
    while aux < sales:
        print("1")
        for i in range(interval_size):
            aux2 += listofsales[i + aux]
            if i + aux == sales + 1 - interval_size:
                ans = aux2/(interval_size)
                aux += interval_size

        
gen_avg = list(avg(n,k,v))

low_avg = min(avg(n, k, v))
max_avg = max(avg(n, k, v))


print(f"{gen_avg.index(low_avg) + 1} {gen_avg.index(max_avg) + 1}")

