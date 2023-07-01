n=int(input())
l=list(map(int,input().split()))
b=sum(l)//n
c=0
for i in l:
    if(i>=b):
        c+=1
print(c)