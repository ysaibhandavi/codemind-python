a=input()
b=[]
for i in a:
    if i.isdigit():
        b.append(i)
c=(len(b))
if c==0:
    print("Doesn't contain digit")
else:
    print("Contains %d digit"%c)
    


    