a=input()
b=[]
for i in a:
    if i.isdigit():
        b.append(int(i))
print(sum(b))