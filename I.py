from collections import deque

d = input()
g = input()


def substrings(x):
    strlen= 0
    for i in range(len(d)):
        aux = ""
        strlen += 1
        for j in range(strlen):
            aux += d[j]    
            yield aux        


y = list(substrings(d))


print(y)

