s=int(input())
l=list(map(int,input().split()))
c=[]
for i in l:
    if(i%2==0):
        c.append(i)
        d=len(c)
        e=d-1
        f=c[1:e:]
print(len(f))


    
    
    
        