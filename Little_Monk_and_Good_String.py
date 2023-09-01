s=input()
a="aeiou"
c=[]
d=0
for i in s:
    if i in a:
        d+=1
        c.append(d)
    else:
        d=0
print(max(c))
        