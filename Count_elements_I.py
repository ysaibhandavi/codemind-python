n,m=map(int,input().split())
n=list(map(int,input().split()))
m=list(map(int,input().split()))
a=set(n)
b=set(m)
print(len(list(a&b)))