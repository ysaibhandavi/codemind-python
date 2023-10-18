a=input().lower().replace(" ","")
b=input().lower().replace(" ","")
c=[]
for i in a:
    if i in b:
        c.append(i)
for i in b:
    if i in a:
        c.append(i)
p=sorted(set(c))
if(len(c)>=1):
    print("".join(p))
else:
    print("-1")

        