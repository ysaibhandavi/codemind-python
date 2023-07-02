n=int(input())
l=list(map(int,input().split()))
b=set(l)
c=0
for i in b:
    if i in b:
        c+=i
print(c)
        