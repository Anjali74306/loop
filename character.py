n=int(input("enter number of alphabet"))
i=1
while i<=n:
    j=1
    a=65
    while j<=n:
        print(chr(a,),end=" ")
        j=j+1
        a=a+1
    print()
    i=i+1    