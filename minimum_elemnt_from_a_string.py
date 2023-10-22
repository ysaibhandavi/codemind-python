n=input().split()
for i in n:
    n=list(sorted(i))
    a=n[0]
    s=n[1:]
    p=a.lower()
if p in s:
    print(p)
else:
    print(a)