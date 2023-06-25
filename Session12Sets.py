#****************************************** Intro to sets **********************************************
""" set data type 
unordered collection of unique item """

# s = {1,2,3,2}
# print(s)                            # {1, 2, 3}    --> repeated item do not print

# l=[1,2,3,4,4,5,5,5,6,7,7,8]
# s1 = set(l)                           # --> removes same element
# print(s1)                            # {1, 2, 3, 4, 5, 6, 7, 8}
 
# s1 = list(set(l))                    # list after removing same element 
# print(s1)                           # [1, 2, 3, 4, 5, 6, 7, 8]

# s.add(4)
# print(s)                               # {1, 2, 3, 4}

# s.remove(3)
# print(s)                                       # {1, 2}


#******************************************** more about sets ******************************************
# s = {'a','b','c'}

""" in keyword """
# if 'a' in s:
#     print('present')
# else:
#     print('absent')

""" for loop """
# for item in s:
#     print(item)                       # --> output will change after refreshing

""" set method """
# 1. union
# 2. intersection

# s1 = {1,2,3,4}
# s2 = {3,4,5,6}

# union_set = s1 | s2
# print(union_set)                        # {1, 2, 3, 4, 5, 6}

# int_set = s1 & s2
# print(int_set)                            # {3, 4}






















































