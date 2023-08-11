from collections import deque


n, q = [int(i) for i in input().split()]

v = [int(i) for i in input().split()]

op = deque()

for i in range(q):
    op.append([int(i)for i in input().split()])

v_values = deque([v])

for i in range(len(op)):
    # print(f"op[0]: {op[0]}")
    if op[i][0] == 1:
        for j in range(op[i][1] - 1,op[i][2]):
            # print(f"op[i][1] e op[i][2]: {op[i][1]} e {op[i][2]}")
            v[j] += op[i][3]
        v_values.append(v)
        print(f"v_values:{v_values}")
    else:
        optimistic = deque()
        for p in range(len(v)):
            aux = []
            for k in range(len(v_values)):
                aux.append(v_values[k][p])
                if k == len(v_values) - 1:
                    gen = (x for x in aux)
                    optimistic.append(max(gen))
            print(f"optimistic: {optimistic}")
        


