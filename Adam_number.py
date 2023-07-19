n=int(input())
s1=int(n)*int(n)
r=str(n)[::-1]
s=int(r)*int(r)
r1=str(s)[::-1]
if int(r1)==s1:
    print('True')
else:
    print('False')

