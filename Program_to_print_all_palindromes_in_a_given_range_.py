a=int(input())
b=int(input())
for i in range (a,b+1):
    n=i
    rev=0
    while(n>0):
        rem=n%10
        rev=(rev*10)+rem
        n=n//10
    if(i==rev):
        print(i,end=' ')
    