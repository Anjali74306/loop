num1=int(input("enter the number" ))
num2=int(input("enter the number"))
counter=1
while counter<=num1 and counter<=num2:
    if num1%counter==0 and num2%counter==0:
        pass
    counter+=1
print(counter-1,"is the highest common factor")