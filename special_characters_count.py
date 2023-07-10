n=input()
c=0
for i in n:
    if i not in "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM ":
        c+=1
print(c)
        