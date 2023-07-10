n=input().split()
a="aeiouAEIOU"
d=[]
for i in n:
    c=0
    for j in i:
        if j in a:
            c+=1
    d.append(c)
e=[]
for i in d:
    if i==max(d):
        e.append(i)
print(len(e))