a=input().lower().replace(" ","")
b=input().lower().replace(" ","")
c=[]
for i in a :
    if i not in b:
        c.append(i)
for i in b:
    if i not in a:
        c.append(i)
p=(sorted(set(c)))
print("".join(p))