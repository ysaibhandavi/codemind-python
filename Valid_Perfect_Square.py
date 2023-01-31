import math
t=int(input())
for i in range(t):
    n=int(input())
    k=int(math.sqrt(n))
    if k*k==n:
        print("True")
    else:
        print("False")
