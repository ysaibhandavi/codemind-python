n=int(input())
l=list(map(int,input().split()))
c=[]
d=[]
e=n//2+1
for i in l:
    if(i>=e):
        c.append(i)
    else:
        d.append(i)
if(len(c)==len(d)):
    print(sum(d))
    print(sum(c))
else:
    print(sum(d))
    print(sum(c))
    