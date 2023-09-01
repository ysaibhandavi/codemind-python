t=int(input())
for i in range(t):
    s=input()
    b=s[::-1]
    if s==b and len(s)%2==0:
        print("YES","EVEN")
    elif s==b and len(s)%2!=0 :
        print("YES","ODD")
    else:
        print("NO")
    