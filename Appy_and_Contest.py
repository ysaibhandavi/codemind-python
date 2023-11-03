t=int(input())
for i in range(t):
    n,a,b,k=map(int,input().split())
    c=0
    d=0
    e=0
    c=n//a
    d=n//b
    e=n//(a*b)
    p=(c+d)-e
    if(p>=k):
        print("Win")
    else:
        print("Lose")