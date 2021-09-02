
row=int(input("Enter the number"))
i=0
z=0
while i<=row:
    j=1
    while j<=row-i:
        print(" ",end='')
        j=j+1
    j=0
    while j<=z:
        print(i,end='')
        j=j+1
    z=z+2
    print() 
    i=i+1   