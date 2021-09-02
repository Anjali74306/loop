
# # c = 0
# # d = 1
# # while c < 3:
# #     c = c + 1
# #     d = d * c
# #     print ("Loop Ke Andar") 
# # else:
# #     print ("Loop Ke Bahar")


# # n = 6
# # s = 0
# # i = 1
# # while i <= n:
# #     s = s + i
# #     i = i + 1
# #     print (s)

# n=int(input("enter the number"))
# x=0
# y=1
# z=0
# while (z<=n):
#     print(z)
#     x=y
#     y=z
#     z=x+y


a,b=0,1
counter=0
while counter<100:
    if counter==0:
        print(0)
    print(b)
    a,b=b,a+b
    counter=counter+1
