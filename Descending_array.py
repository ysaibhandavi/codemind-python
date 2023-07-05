n=int(input())
l=list(map(int,input().split()))
s=sorted(l)
s=s[::-1]
if(s==l):
    print('yes')
else:
    print('no')
    