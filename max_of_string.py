a=input()
b=[]
for i in range (0,len(a)):
    b.append(ord(a[i]))
print(chr(max(b)))
    
