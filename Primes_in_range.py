a=int(input())
b=int(input())
c=0
for num in range(a,b+1):
    if num>1:
        for i in range(2,int(num**0.5)+1):
            if(num%i==0):
                break
        else:
            c+=1
if(c>=2):
    print(c)
