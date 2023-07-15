n=int(input())
l=list(map(int,input().split()))
c=[]
p=[]
for i in l:
    i=list(str(i))
    c.append(len(i))
m=max(c)
for i in l:
    i=list(str(i))
    if(len(i)==m):
        i="".join(i)
        p.append(i)
print(*p)