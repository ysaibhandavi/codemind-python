n=int(input())
f3=0
f1=1
f2=1
if(n==0 or n==1):
    print('True')
else:
    #generating the fibnocci number until the number is less than nif (n)
    while f3<n:
        f3=f2+f1
        f2=f1
        f1=f3
    if(f3==n):
        print('True')
    else:
        print('False')