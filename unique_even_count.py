n=int(input())
l=list(map(int,input().split()))
b=set(l)
c=0
for i in b:
    if(i%2==0):
        c+=1
print(c)
        
    