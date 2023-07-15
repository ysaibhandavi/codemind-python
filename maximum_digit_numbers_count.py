n=int(input())
l=list(map(int,input().split()))
c=[]
e=[]
for i in l:
    m=list(str(i))
    c.append(len(m))
d=max(c)
for i in l:
    i=list(str(i))
    if(len(i)==d):
        i="".join(i)
        e.append(i)
print(*e)
    
    