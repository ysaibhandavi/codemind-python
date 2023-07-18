a=int(input())
m,n=0,1
print(m,n,end=" ")
for i in range(2,a):
    o=m+n
    m=n
    n=o
    print(o,end=" ")
