n=input()
p=input()
c=0
for i in n:
    if(i==p):
        c+=1
if c>=1:
    print(c)
else:
    print('-1')
    