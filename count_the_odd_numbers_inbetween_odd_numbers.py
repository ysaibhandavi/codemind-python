n=int(input())
l=list(map(int,input().split()))
c=[]
for i in range(1,len(l)-1):
    if (l[i]%2!=0 and l[i+1]%2!=0 and l[i-1]%2!=0):
        c.append(i)
print(len(c))
    
    