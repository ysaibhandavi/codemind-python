n=int(input())
l=list(map(int,input().split()))
c=[]
for i in l:
    if (i>=0):
        m=list(str(i))
        c.append(len(m))
        d=min(c)
e=0
for i in c:
    if(i==d):
        e+=1
print(e)
        