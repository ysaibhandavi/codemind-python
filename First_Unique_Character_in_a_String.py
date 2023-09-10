s=input()
n=list(s)
for i in n:
    if n.count(i)==1:
        print(n.index(i))
        break
else:
    print(-1)