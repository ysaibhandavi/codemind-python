n=int(input())
l=list(map(int,input().split()))
m=len(l)
s=0
for i in l:
    m=m-1
    if i>0:
        a=2**m
        s=s+a
print(s)
        