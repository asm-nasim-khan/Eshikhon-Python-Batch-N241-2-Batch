# Object Oriented Programming
# 1. Encapsulation
# 2. Abstraction
# 3. Inheritence
# 4. Polymorphism

# Funtion vs Method

# class Animal:
#     def __init__(self,eyeinput): #Constructor
#         print("Object Created")
#         self.__eyes = eyeinput

#     def sound(self):
#         print("Meow Meow")

#     def getter(self):
#         return self.__eyes

# #Main Class
# cat = Animal(2)
# dog = Animal(1)
# print(cat.getter())

# # print(dog.eyes)


# class Bird:
#     def __init__(self): #Constructor
#         print("Object Created")
    
#     def flight(self):
#         print("Flying...")

# class cuckoo(Bird):
#     def __init__(self): #Constructor
#         print("Cuckooo Created")

#     def sing(self):
#         print("Lalalala...")


# class penguin(Bird):
#     def __init__(self): #Constructor
#         print("Penguin Created")
    
#     def flight(self): #Method Overriding
#         print("Can not Fly...")

# pg = penguin()
# pg.flight()

# from abc import ABC,abstractmethod

# class Bird(ABC):

#     @abstractmethod
#     def flight(self):
#         pass

# class cuckoo(Bird):
#     def sing(self):
#         print("Lalalala...")
    
#     def flight(self):
#         print("Flying")

# cu= cuckoo()
# cu.flight()




class Mobile:
    def __init__(self):
        self.camera = 5
        self.sim = 2


Samsung_A90 = Mobile()
Iphone_70 = Mobile()
Iphone_70.camera = 500
Iphone_70.sim = 40
Iphone_70.spekear = 90
print(Iphone_70.camera)
print(Samsung_A90.camera)
print(Iphone_70.spekear)




