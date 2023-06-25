""" with the help of this we can create list in min. line"""

""" create  a list of squares from 1 to 10"""
# squares = []
# for i in range(1,11):
#     squares.append(i**2)
# print(squares)                            # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

"""list comprehension"""
# square1 = [i**2 for i in range(1,11)]
# print(square1)                           # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#*********************************************************************************************

# negative = [-i for i in range(1,11)]
# print(negative)                           # [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]

#*****************************************************************************************************

"""add first char of words in list """
# names = ['deven','rahul','sharyu']
#['d','r','s']
# new_list = []
# for i in names:
#     new_list.append(i[0])
# print(new_list)                           # ['d', 'r', 's']

"""list comprehension"""
# new_list2 = [i[0] for i in names]
# print(new_list2)


#********************************************* Ex 1 ***********************************************
"""def a function that take a list of strings 
and reverse the string containing in list
NOTE - use list comprehension """

# def rev_string(l):
#     return [name[::-1] for name in l]

# print(rev_string(['abc','tuv','xyz']))                     # ['cba', 'vut', 'zyx']


#******************************************** if statement ******************************************
# numbers = list(range(1,11))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#even nums =[2,4,6]
# nums = []
# for i in numbers:
#     if i%2 == 0:
#         nums.append(i)
# print(nums)                                         # [2, 4, 6, 8, 10]

"""list comprehension"""
# even_num = [i for i in numbers if i%2 == 0]
# even_num = [i for i in range(1,11) if i%2 == 0]
# print(even_num)                                    # [2, 4, 6, 8, 10]


#*************************************** Ex 2 ********************************************
""" input -->  [True, False, [1,2,3,'xyz'], 1, 4.5, 6]
    output --> ['1', '4.5', '6']"""

# def num_to_string(l):
#     return [str(i) for i in l if (type(i) == int or type(i) == float)]

# input =  [True, False, [1,2,3,'xyz'], 1, 4.5, 6]
# print(num_to_string(input))                              # ['1', '4.5', '6']


#**************************************** if else ******************************************
# nums = [1,2,3,4,5,6,7,8]
# new_list = [-1,4,-3,8]                     # --> odd = negative & even = even * 2

# new_list = []
# for i in nums:
#     if i%2 == 0:
#         new_list.append(i*2)
#     else:
#         new_list.append(-i)
# print(new_list)                                    # [-1, 4, -3, 8, -5, 12, -7, 16]

""" list compre. """
# new_list2 = [i*2 if (i%2 == 0) else -i for i in nums]
# print(new_list2)                                   # [-1, 4, -3, 8, -5, 12, -7, 16]


#******************************************** nested list ***************************************
# ex = [[1,2,3], [1,2,3], [1,2,3]]

# nested_list = [[i for i in range(1,4)] for j in range(3)]
# print(nested_list)                                  # [[1, 2, 3], [1, 2, 3], [1, 2, 3]]


list_1 = [1,3,5,2,7,4,8,5]
list_2 = [1,4,2,6,9,5,8,3]

new_list = [i for i in list_1 if i in list_2]
print(new_list)
