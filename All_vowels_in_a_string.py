s=input()
a='aeiou'
c=[]
for i in a:
    if i in s:
        c.append(i)
if(len(c)==len(a)):
    print('True')
else:
    print('False')