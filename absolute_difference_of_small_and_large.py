n=input().split()
for i in n:
    p=min(i)
    q=max(i)
    p=abs(ord(q)-ord(p))
    print(p,end=" ")