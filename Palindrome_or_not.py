n=input().lower()
b=""
for i in n:
    if i.isalnum():
        b+=i
if b==b[::-1]:
    print("True")
else:
    print("False")
    
    