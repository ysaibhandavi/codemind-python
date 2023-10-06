n=int(input())
c=[]
d=[]
for i in range(1,n+1):
    f=0
    for j in range(1,n+1):
        if(i%j==0):
            f+=1
    if (f==2):
        c.append(i)
for k in c:
    for l in range(len(c)):
        if k*c[l]==n:
            d.append(k)
            d.append(c[l])
if(len(d)>0):
    print(d[0],d[1])
else:
    print('-1')
        
        