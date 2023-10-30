n=int(input())
l=list(map(int,input().split()))
k=sum(l)
if(k%2==0):
    print("1")
else:
    print("0")