t=int(input())
for _ in range(t):
    l,r=map(int,input().split())
    c=0
    for i in range(l,r+1):
        a=i%10
        if a==2 or a==3 or a==9:
            c+=1
    print(c)