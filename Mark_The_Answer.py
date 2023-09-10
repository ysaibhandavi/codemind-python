n,m=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in l:
    if m<=i:
        c+=1
print(c)