n=int(input())
l=list(map(int,input().split()))
p=[]
for i in l:
    if(i>=0):
        s=list(str(i))
        p.append(len(s))
    else:
        t=list(str(i))
        p.append(len(t)-1)
print(*p)