from math import factorial

n=int(input("pascal trianglr for how many rows?"))
for i in range(n+1):
    for j in range(n-i+1):
        print(end=" ")
for k in range(i+1):
    ele = factorial(i)/(factorial(k)*factorial(i-k))
    print(int(ele),end=" ")
    print()