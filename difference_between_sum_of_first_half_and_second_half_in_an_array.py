n=int(input())
l=list(map(int,input().split()))
c=[]
d=[]
for i in l:
    if(i<=n/2):
        c.append(i)
    else:
        d.append(i)
e=sum(c)
f=sum(d)
print(f-e)
        
    
    


