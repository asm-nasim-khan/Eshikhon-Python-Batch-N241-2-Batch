# print("Good Morning")


# def My_name():
#     print("Hello")

# print("Good Night")
# name()
# print("Evening")

# lst = ['Nasim',"sakib","Rakib"]
# def greetings(name):
#  print("semd Email to ",name)

# for i in lst:
#  greetings(i)

# def greetings(name,age=15):
#  print("Hello ",name)
#  print("Youre ",age)


# user = input("Enter name: ")
# greetings(user)


# Start
# stop 
# step 


def Range(*args):
    start = 0
    stop = 0
    step = 0
    if len(args) == 1:
        start = 0
        stop = args[0]
        step = 1
    elif len(args) == 2:
        start = args[0]
        stop = args[1]
        step = 1
    elif len(args) == 3:
        start = args[0]
        stop = args[1]
        step = args[2]
    print("start",start)
    print("Stop",stop)
    print("step",step)

Range(10,100,2)



