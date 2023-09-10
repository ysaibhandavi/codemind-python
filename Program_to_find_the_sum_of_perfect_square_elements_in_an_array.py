n=int(input())
l=list(map(int,input().split()))
c=[]
d=max(l)
for i in range(d):
    i=i*i
    if i in l:
        c.append(i)
print(sum(c))
