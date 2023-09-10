n=int(input())
l=list(map(int,input().split()))
l=set(l)
l=sorted(l)
p=l[::-1]
if (n>2):
    print(p[2])
else:
    print(max(l))