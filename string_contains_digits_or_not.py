t=int(input())
for i in range (t):
    a=input()
    c=0
    for j in a :
        if j in "1234567890":
            c+=1
    if c>0:
        print('Yes')
    else:
        print('No')