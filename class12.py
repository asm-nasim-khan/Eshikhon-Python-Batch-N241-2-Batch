

# for i in range(1,50,1):
#     if i%2==1:
#         print(i)


#start
#stop
#step

# for x in range (1,51,2):
#     print(x)
#[10,9,8,7,6,5,4,3,2,1]
# x = 10  
# while x>0:
#     print(x)
#     x = x - 1
# print("End")
# x = 1
# while x<11:
#     print(x)
#     x = x + 1
# print("End")
# for x in range(0,11): #[0,1,2,3,4,5,6,7,8,9,10]
#     print(x)


# for x in range(0,10,1):#[0,1,2,3,4,5,6,7,8,9]
#     if x == 5:
#         pass
#     print(x)



# num = 16
# x = 1
# while x <= num:
#     if num % x == 0:
#         print(x)
#     x = x + 1


# infinity Loop

while 1:
    user = input("Enter: ")
    if user == "stop":
        break
    else:
        print(user)

msg2  = ["H","a","p","p","y"]

# for element in msg2: #for each loop
#     print(element)
# print(len(msg2))

# for idx in range(len(msg2)): #for each loop
#     print(msg2[idx])


# for i in range(55,91,5):
#     if i == 90:
#         print(i,end="")
#     else:
#         print(i,end=",")

b = 0
p = 0

while 1:
    print("Enter 1 for Burger \nEnter 2 for Pizza \nstop for Results")
    print("================================================================")
    user = input("Enter: ")
    if user == "stop":
        print("Burger",b)
        print("Pizza",p)
        break
    else:
        if int(user) == 1:
            b+=1
        elif int(user)==2:
            p+=1










