n=list(map(str,input().split()))
c=[]
for i in range(len(n)):
    if (i%2==0):
        i=str(n[i])
        c.append(i[::-1])
    else:
        c.append(n[i])
print(*c)
    