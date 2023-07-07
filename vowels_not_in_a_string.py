s=input()
a="aeiou"
c=[]
for i in a:
    if i not in s:
        c.append(i)
if(len(c)==0):
    print(0)
else:
    print(*c)
