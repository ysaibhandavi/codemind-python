n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    c+=i
d=c/n
print('%.2f'%d)
