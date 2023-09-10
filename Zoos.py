n=input()
a=[]
b=[]
for i in n:
    if i=='z':
        a.append(i)
    else:
        b.append(i)
if(len(b)==(2*len(a))):
    print('Yes')
else:
    print("No")
        