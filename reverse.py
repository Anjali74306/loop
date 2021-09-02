user=int(input("enter the number"))
rev=0
while user>0:
    rem=user%10
    rev=rev*10+rem
    user=user//10
print(rev)
rev=rev-1

