n=int(input())
l=list(map(int,input().split()))
c=[]
for i in l:
    m=list(str(i))
    c.append(len(m))
    d=max(c)
e=0
for i in c:
    if d==i:
        e+=1
print(e)
    