str=input()
v=0
c=0
d=0
ws=0
for i in str:
 if(i == 'a'or i == 'e'or i == 'i'or i == 'o'or i == 'u' ):
    v+=1
 elif (i== " "):
    ws+=1
 elif i>='0' and i<='9':
    d+=1
 else:
    c+=1
print("Vowels:",v)
print("Consonants:",c)
print("Digits:",d)
print("White spaces:",ws)