n=input().split()
c=0
for i in n:
    i=i.lower()
    x=i
    x=x[::-1]
    if x==i:
        c+=1
print(c)
        