s=input().split()
a=[]
b=[]
e=[]
for i in s:
    p=min(i)
    a.append(p)
    q=max(i)
    b.append(q)
    for j in i:
        e.append(j)
        
c=min(a)
d=max(b)
print(c,end=" ")
print(e.count(c),end=" ")
print(d,end=" ")
print(e.count(d),end=" ")
    
    
    
    