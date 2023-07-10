s=list(map(str,input().split()))
d=[]
a="aeiouAEIOU"
for i in s:
    c=0
    for j in i:
        if j in a:
            c+=1
    print(c,end=" ")   
