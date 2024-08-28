# class Mobile:
#     Battery = "3000 mAh"
#     def __init__(self,sim):
#         self.msg = "Default"
#         self.sim = sim

#     def __add__(self,obj):
#         new = Mobile(self.sim * obj.sim)
#         new.msg = "Merged Phone"
#         return new
#     def __sub__(self,obj):
#         print("subtracting 2 Objects")
    
#     def __pow__(self,obj):
#         print("Power")
    
#     def __str__(self):
#         return self.msg

#     def print_Details(self):
#         print(self.sim)
#         print(self.msg)

#     def getter(self):
#         return self.sim


# Samsung = Mobile(2)
# vivo = Mobile(3)
# oneplus = Mobile(4)
# # # vivo.print_Details()
# # print(vivo.getter())
# vivo.Battery = "4500 mAh"
# print(Mobile.Battery)
# print(Samsung.Battery)
# print(vivo.Battery)
# Mobile.Battery = "5000 mAh"

# print(Mobile.Battery)

# class Human:
#     def __init__(self,name,gender):
#         self.name = name
#         self.age = 0
#         self.gender = gender

# person_1 = Human("Nasim","male")



class Bank_Account:
    users = []
    def __init__(self,name):
        self.balance = 0
        Bank_Account.users.append(name)
        self.name = name
    
    def add_Money(self,amount):
        self.balance += amount

    def withdraw_Money(self,amount):
        if self.balance - amount >=10:
            print(amount,"has withdrawn")
            self.balance = self.balance - amount
        else:
            print("Not Enough Money")

    def check_balance(self):
        print(self.balance)

new_user = Bank_Account("Nasim")
new_user.add_Money(10000)
new_user.withdraw_Money(9990)
new_user.check_balance()