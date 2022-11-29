num=int(input())
n=len(str(num))
s=num*num
l=s%pow(10,n)
if(l==num):
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')


