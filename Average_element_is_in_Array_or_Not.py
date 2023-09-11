n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    c+=i
d=c//7
if d in l:
    print("True")
else:
    print("False")
    