
i=5
while 1<=i:
    guess=int(input("enter the number"))
    if guess==10:
        print("corect ")
    elif guess!=10:
        print("your guess is too less")
    else:
        print("guess is too high")
        break
    i-=1
print("you have only",i ,"chance")




