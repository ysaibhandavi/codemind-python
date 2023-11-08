n=int(input())
s=0
i=0
while n!=0:
    j=n%10
    s=s+j*(8**i)
    n=n//10
    i+=1
print(format(s,'b'))