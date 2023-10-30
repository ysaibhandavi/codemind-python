t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    k=sorted(l)
    if(k==l):
        print(0)
    else:
        print(max(l)-min(l))