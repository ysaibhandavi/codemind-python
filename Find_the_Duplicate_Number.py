n=int(input())
l=list(map(int,input().split()))
c=[]
for i in l:
    if l.count(i)>1:
        c.append(i)
print(max(c))
        