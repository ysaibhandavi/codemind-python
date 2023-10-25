a=int(input())
b=int(input())
for i in range(a,b+1):
    t=i
    c=0
    d=0
    while(t!=0):
        r=t%10
        t=t//10
        c+=1
        if(r==0):
            break
        if(i%r==0):
            d+=1
    if(d==c):
        print(i,end=" ")
            
        
    