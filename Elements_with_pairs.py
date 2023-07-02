n=int(input())
l=list(map(int,input().split()))
c=[]
for i in l:
    c.append(i)
if(n%2==0):
    print(*c)
else:
    c.extend([0])
    print(*c)