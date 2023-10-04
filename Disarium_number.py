n=int(input())
n=str(n)
l=len(n)
n=int(n)
m=n
sum=0
while n>0:
    rem=n%10
    sum=sum+int(rem**l)
    n=n//10
    l=l-1
if m==sum:
    print("True")
else:
    print("False")
