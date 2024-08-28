# Task 3:  
#   Write a program that takes a character (i.e. string of length 1) and returns true if
# it is a vowel, false otherwise.  

# user_inp = input("Enter a char: ")
# vowels = ["a",'e','i','o','u']
# if user_inp.lower() in vowels:
#     print("Vowel")
# else:
#     print("Consonent")

# print("A".lower())


# # Task 1:
# #  Take a number as input from the user and print if 
# # the last digit of that number is divisible by 3. Print Yes or No



'''
======================================================
Bonus: Hints (Change The type into List)
Given Tuple,
mytup = (9,5,6,7)

Add another number to this tuple.

Sample output:
 (9,5,6,7,x)
 '''
# mytup = (9,5,6,7)
# mytup = list(mytup)
# mytup.append("x")
# mytup = tuple(mytup)
# print(mytup)

# def Check_by_3():
#     user_inp = input("Enter a Number: ")
#     num = int(user_inp[-1])
#     if num % 3 == 0:
#         print("Yes")
#     else:
#         print('No')

# Check_by_3()


# *args and **kwargs in Python



# def Test(**name):
#     print(name)

# Test(name = "nasim",age=100,Location = "Dhaka")


# Re cursion

# def Recursion(i):
#     if i == -1:
#         return
#     i = i - 1
#     Recursion(i)
#     print(i) 

# Recursion(5)

#return

# def Our_scope(a):
#     print(a+10)
# Our_scope(1)

# x = lambda a: a+10
# print(x(1))

# x = lambda a,b: a*b
# print(x(9,8))



# x = 5
# x = 7
# print(x)


#return

def Our_scope(a):
    c = a + 10
    return c

d = Our_scope(1)  + 40
if d % 3 == 0:
    print("Yes")
else:
    print("No")
# null
# None





