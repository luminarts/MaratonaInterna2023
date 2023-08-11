n, m = [int(i) for i in input().split()]

crws = 0

# def factorial(k):
#     aux = 1
#     for i in range(k):
#         aux *= k






for i in range(1,n+1):
    aux = m**i - (i-1)**2
    crws += aux


print(crws)

