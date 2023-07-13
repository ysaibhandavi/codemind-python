n=input().split()
c=[]
d=[]
for i in n:
    p=ord(min(i))
    c.append(p)
    q=ord(max(i))
    d.append(q)
print(abs(sum(c)-sum(d)))