# data = ["apple",23,78.34]
# print(data[0:2])


# data = [23,5,81,9,83,7,10,4,7,135,23,6]
# data.sort()
# data.reverse()
# print(data)

# print(data[-1::-1])
# data.append([1,2])
# print(data)
# data.extend([3,8,34,2])
# print(data)
# data.pop(2)                                       # --> works on indice elements
# print(data)


#*************************************intro to list**************************************
""" can store any data types values """

# mixed=[1,2,3,4,"five","six",2.3,None]
# print(mixed[6])                      #2.3

# mixed[1]="two"
# print(mixed)                       #[1, 'two', 3, 4, 'five', 'six', 2.3, None]


#************************************add data to list********************************
# fruits1=['mango','orange']
# fruits2=['grapes','apple']
# fruits1.append('grapes')
# print(fruits1)                      #['mango', 'orange', 'grapes']

# fruits1.extend(['banana','melon'])    #['mango', 'orange', 'banana', 'melon']
# print(fruits1)

# fruits1.insert(1,"melon")
# print(fruits1)                       #['mango', 'melon', 'orange']

# fruits = fruits1 + fruits2
# print(fruits)                      #['mango', 'orange', 'grapes', 'apple']

# fruits1.extend(fruits2)
# print(fruits1)                        #['mango', 'orange', 'grapes', 'apple']


#***********************************delete data**************************************

# fruits=['orange','apple','pear','banana','kiwi']
# fruits.pop()
# print(fruits)                   #['orange', 'apple', 'pear', 'banana']

# fruits.remove('banana')
# print(fruits)
 
    

#************************************* in keyword*************************************
# fruits=['orange','apple','pear','banana','kiwi','apple','banana']
# if 'apple' in fruits:
#     print('present')
# else:
#     print('absent')


# fruits=['orange','apple','pear','banana','kiwi','apple','banana']
# print(fruits.count('apple'))               #2

# # fruits.sort()
# # print(fruits)                         #alpabetical order

# numbers=[3,5,1,9,10]
# numbers.sort()
# print(numbers)                         #[1, 3, 5, 9, 10]
# print(sorted(numbers))                 #-----''---------

# numbers.remove(3)
# print(numbers)                         # [5, 1, 9, 10]

# numbers.clear()
# print(numbers)                           #[]

# numbers_copy=numbers.copy()
# print(numbers_copy)                     #[3, 5, 1, 9, 10]


#************************************* 'is' vs '==' *********************************
# fruits1=['orange','apple','pear']
# fruits2=['banana','kiwi','apple','banana']
# fruits3=['orange','apple','pear']

# # print(fruits1 == fruits2)                #False
# print(fruits1 == fruits3)                  #True
# print(fruits1 is fruits3)                 #false    --> is checks whether two list are in same location or not


#**************************************join_split**********************************
"""split method"""
"""convert string --> list"""
# user_info="deven 24".split(' ')
# print(user_info)                        #['deven', '24']

# user_info="deven,24".split(',')
# print(user_info)                          #['deven', '24']
 

"""join method"""
"""convert list --> string"""
# user_info=['deven','67']
# print(' '.join(user_info))              #deven 67
# print(','.join(user_info))              #deven,67


#************************************** list vs string*********************************

"""strings are immatuable
list are mutable"""

# s='string'
# s.title()
# print(s)                        #string

# t=s.title()
# print(t)                        #String

# l=['word1','word2','word3']
# l.pop()
# print(l)                          #['word1', 'word2']


#**************************************** loops on list******************************************
fruits=['orange','apple','pear','banana','kiwi']

# for i in fruits:
#     print(i)

# i=0
# while i < len(fruits):
#     print(fruits[i])
#     i+=1


#************************************* list inside list****************************************
# matrix=[[1,2,3], [4,5,6], [7,8,9]]
# # print(matrix[0])

# # for i in matrix:
# #     for j in i:
# #         print(j,end=" ")                    #1 2 3 4 5 6 7 8 9 

# print(matrix[1][1])                         #5


#************************************* more list**********************************
# # number= list(range(1,11))
# number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # print(number)                                 #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # popped_item=number.pop()                       #10
# # print(number)                                 #[1, 2, 3, 4, 5, 6, 7, 8, 9]

# # print(number.index(1))                         #0

# def negative_list(l):
#     negative=[]
#     for i in l:
#         negative.append(-i)
#     return negative

# print(negative_list(number))                #[-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]


#*******************************************Ch-5...Ex1*************************************
"""def a function which will take list containing numbers as input
and return list containing square of every elements"""

# user=int(input("Enter number upto which list to append : "))
# numbers = list(range(user))

# def square_list(l):
#     square=[]
#     for i in l:
#         square.append(i**2)
#     return square

# print(square_list(numbers))


#*************************************** Ex 2 **********************************************
"""[1,2,3,4]  --> [4,3,2,1]
try to do with append and pop method"""

# def reverse_list(l):
#     l.reverse()
#     return l                                             #[4, 3, 2, 1]

# def reverse_list(l):
#     return l[::-1]                                        #[4, 3, 2, 1]


# def reverse_list(l):
#     r_list=[]
#     for i in range(len(l)):
#         popped_item=l.pop()
#         r_list.append(popped_item)
#     return r_list                                         #[4, 3, 2, 1]

# numbers=[1,2,3,4]
# print(reverse_list(numbers))                             


#***************************************** Ex 3 *********************************************
"""def a function that take list of words as argument and
return list with reverse of every element in that list
ex :  ['abc','tuv'] -->  ['cba','vut']"""

# def reverse_elements(l):
#     elements=[]
#     for i in l:
#         elements.append(i[::-1])
#     return elements

# words = ['abc','tuv','xyz']
# # print(reverse_elements(words))                           # ['cba', 'vut', 'zyx']


#*************************************** Ex 4 *********************************************
"""filter odd even 
input list -> [1,2,3,4,5,6,7]
output ---> [[1,3,5,7], [2,4,6]]"""

# def odd_even(l):
#     odd_nums = []
#     even_nums = []
#     for i in l:
#         if i % 2 == 0:
#             even_nums.append(i)
#         else:
#             odd_nums.append(i)
#     output = [odd_nums , even_nums]
#     return output                                  

# nums = [1,2,3,4,5,6,7]
# print(odd_even(nums))                              #[[1, 3, 5, 7], [2, 4, 6]]


#************************************** Ex 5 *******************************************
"""def a function which take 2 list as input and retrun a list
which contains"""

# def common(l1,l2):
#     output = []
#     for i in l1:
#         if i in l2:
#             output.append(i)
#     return output

# print(common([1,2,5,8], [1,2,7,6]))                  #[1,2]


#************************************* Min and Max ************************************
# num=[1,6,2]
# # print(min(num))                      #1
# # print(max(num))                      #6

# def great_diff(l):
#     return max(l) - min(l)
    
# print(great_diff([25,56,6]))                       #50


#************************************* Ex 6 *********************************************
"""print total lists present inside list
ex : [1,2,3, [1,2], [3,4]] -->2 """

# def sublist(l):
#     count = 0
#     for i in l:
#         if type(i) == list:
#             count += 1
#     return count

# mixed = [1,2,3, [1,2], [3,4]]                         #2
# print(sublist(mixed))


