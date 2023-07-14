s1=input()
s2=input()
l1=list(s1.lower().split())
l2=list(s2.lower().split())
c=[]
for i in l2:
    if i  in l1:
        c.append(i)
print(*c)
        