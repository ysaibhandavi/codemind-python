n=input()
c=0
d=[]
for i in n:
    if i in "aeiou":
        c+=1
        d.append(c)
    else:
        c=0
print(max(d))

        
    