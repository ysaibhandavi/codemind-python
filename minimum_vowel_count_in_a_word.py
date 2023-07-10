n=input().split()
a="aeiouAEIOU"
d=[]
for i in n:
    c=0
    for j in i:
        if j in a:
            c+=1
    d.append(c)
print(min(d))
            