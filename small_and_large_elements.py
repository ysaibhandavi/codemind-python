n=input().split()
a=[]
b=[]
for i in n:
    p=min(i)
    a.append(p)
    q=max(i)
    b.append(q)
print(*a[:1],end=" ")
print(b[-1],end=" ")
