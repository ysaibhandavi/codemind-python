n=int(input())
c=[]
d=[]
for i in range(1,n+n):
    f=0
    for j in range(1,n+n):
        if(i%j==0):
            f+=1
    if(f==2):
        c.append(i)
for k in c:
    if k-n>0:
        d.append(k-n)
    else:
        d.append(n-k)
print(min(d))
        
        