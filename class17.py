# List Comprehension

# newList = [ expression(element) for element in oldList if condition ] 


# newList = [ Kaj for element in oldList Filter ] 

lst1 = [1,2,3,4,5,6,7,8]


lst2 = [elem ** 3 for elem in lst1 ]


even_list = [elem for elem in lst1 if elem % 2 == 0 ]




odd_list = [x for x in range(10) if x % 2 == 1 ]


# print(odd_list)



# for elem in lst1:
#     lst2.append(elem*elem)



# print(lst2)
# print(even_list)

lst1 = [1,2,3,4,5,6,7,8]

# test = [print(x) for x in lst1]

# set_1 = {1,2,3,4,5,6,7,8}
# new_set= {x**2 for x in set_1}

# print(new_set)

# set_old={1,2,3,4,5}
# set1=(s*s for s in set_old)
# print(set1)

# tup=(1,2,3,4,5,)
# print(id(tup))
# # tup = tup + (65,23,3,45,)
# tup+=(65,23,3,45,)
# print(id(tup))


dict_1  = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# for k in dict_1.keys():
#     print(k,dict_1[k])

dict_1  = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
dict_2 = {x:y for x,y in dict_1.items() if y % 2 == 1 and x == "a"}
print(dict_2)

# import datetime as dt

# x = dt.datetime.now()
# print(x)

import math

# print(math.sqrt(2))

# print(math.pi)
# print(2/math.inf)

import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
print(y)




