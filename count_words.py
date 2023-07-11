n=list(map(str,input().split()))
c=0
for i in n:
    if i[0] in "aeiouAEIOU":
        c+=1
print(c)
        

