# num1 = int(input('enter number : '))
# num2 = int(input('enter number : '))
# sum = num1 + num2
# print('sum of',num1,'and',num2,'is :',sum )
# print(f'sum of {num1} and {num2} is {sum}')


# print(4 + 3 % 5)

# num_list = input('enter list of numbers separated by space : ').split()
# print(num_list)
# num_list = [int(num) for num in num_list]
# sum = sum(num_list)
# print('sum is : ',sum)

# str_list = input('enter no of strings separated by spaces : ').split()
# str_list = [len(string) for string in str_list]
# max_length = max(str_list)
# print('max length string is : ',max_length)

# num_list = input('enter list of numbers separated by space : ').split()
# num_list = [int(num) for num in num_list]
# num_list.sort(reverse=True)
# print(num_list)

# str = input('enter string : ')
# vowels = "aeiouAEIOU"
# count = 0
# for char in str:
#     if char in vowels:
#         count += 1
# print('count : ',count)    

# num_list = input('enter list of numbers separated by space : ').split()
# num_list = [int(num) for num in num_list]
# even_list = [num for num in num_list if num % 2 == 0]
# print(even_list)
# sum_list = sum(even_list)
# print(sum_list)


# string = input('enter string : ')
# vowels='aeiouAEIOU'
# for i in string:
#     if i in vowels:
#         str=string.replace(i,"")
# print(str)


# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print(" ")




"""take a list from user and return product of largest three numbers""" 
# def great_prod(l):
#     l.sort()                                   #[1,2,4,6,7]
#     n = len(l)
#     # print(l[n-1]* l[n-2]* l[n-3])
#     return l[-1]*l[-2]*l[-3]

# print(great_prod([1,4,6,2,7]))               #7*6*4 = 168


"""Creating 3 functions
# 1. Return the highest score
# 2. Return the lowest score
# 3. Return the list in the sorted manner

students = [('Magnus', 85), ('Max', 90), ('Charlie', 80), ('Raven', 75), ('Silver', 70),('Alice',95)]"""


# def high(l):
#     toppername, highestscore = l[4]                          # assume l[4]
#     for i in l:
#         name, score = i
#         if score > highestscore:
#             toppername = name
#             highestscore = score
#     return (toppername, highestscore)

# print(high([('Magnus', 85), ('Max', 90), ('Charlie', 80), ('Raven', 75), ('Silver', 70),('Alice',95)]))


# def min(l):
#     dropername, lowestscore = l[4]
#     for i in l:
#         name, score = i
#         if score < lowestscore:
#             dropername = name
#             lowestscore = score
#     return (dropername, lowestscore)

# print(min([('Magnus', 85), ('Max', 90), ('Charlie', 80), ('Raven', 75), ('Silver', 70),('Alice',95)]))

# def sort_(l):
#     sorted(l[0])
#     return sorted

# print(sort_([('Magnus', 85), ('Max', 90), ('Charlie', 80), ('Raven', 75), ('Silver', 70),('Alice',95)]))


"""# Given a string, you have to determine the alphabets that are present in it.
# Also if possible, try to identify which vowels are present as well
in given string"""

# def getFrequenncy(str):
#     str.lower()
#     vowels = 'aeiou'
#     dict = {}
#     for char in str:
#         if char in vowels:
#             dict[char] = str.count(char)
#     alphabets = set(str)
#     return dict
    

# string = "JSPM colleges are committed to provide value based quality education"
# print(getFrequenncy(string))



"""euclidean distance
given 2 pints in space ,a(x1,y1) and b(x2,y2) you have to find distnace
between them
formula = sqrt((x2-x1)^2 + (y2-y1)^2)"""

# import math

# def euclidean(p1,p2):
#     x1,y1 = p1
#     x2,y2 = p2
#     distance = math.sqrt( (x2-x1)**2 + (y2-y1)**2 )
#     return distance

# p1 = (1,5)                                     
# p2 = (6,3)                                     
# print(euclidean(p1,p2) )                                     


"""# You have the dataset of the list of friends of 3 users.
# You have to determine which all people are friends of all the 3 users.
# You also have to find the non-common friends
# """
# Alice_friends = {'Magnus', 'Max', 'Charlie', 'Agatha', 'Bob'}
# Bob_friends = {'Violet', 'Collei', 'Magnus', 'Charlie', 'Alice'}
# Charlie_friends = {'Alice', 'Bob', 'Violet', 'Agatha', 'Magnus'}

# Alice_friends.add('Alice')
# Bob_friends.add('Bob')
# Charlie_friends.add('Charlie')

# def common_friends(s1,s2,s3):
#     common = s1&s2&s3                                # & -> common in 3 sets
#     print("common friends : ",common)

# def uncommon_friends(s1,s2,s3):
#     uc = []
#     for i in s1:
#         if i not in s2 and s3:
#             uc.append(i)
#     for i in s2:
#         if i not in s1 and s3:
#             uc.append(i)
#     for i in s3: 
#         if i not in s1 and s2:
#             uc.append(i)
#     uncommon = set(uc)
#     print("uncommon friends : ",uncommon)

# common_friends(Alice_friends,Bob_friends,Charlie_friends)
# uncommon_friends(Alice_friends,Bob_friends,Charlie_friends)


"""# Sorting items in a list based upon a certain attribute
items = [
  # ("Item_name", CP, SP, Quantity)
    ("Blue ink pens", 16, 20,  286 ),
    ("Black ink pens", 18, 20, 726),
    ("100 Page books", 25, 30, 678),
    ("500 Page books", 65, 80, 814),
    ("Erasers", 3, 6, 369),
    ("Pencils", 6, 10, 312)
]

# Sort by Profit earned in each item
# Sort by Quantity
# Give the costliest item in the itemset
# Give the cheapest item in the itemset
# Give the item that gives the most profit
# Give the item that gives the least profit"""


# def profit(sp,cp):
#     l = ()
#     for i in (sp and cp):
#         profit = sp-cp
#         l.append(profit)
#     return l

# print(profit( (20,20,30,80,6,10),(16,18,25,65,3,6) ))


def quantity(l1):
    l1.sort()
    return (f"sorted : {l1}")
print(quantity([286,726,678,814,369,312]))


def cost(l1):
    high = l1[0]
    for i in l1:
       if i > high:
           high = i
    return (f"costliest item : {high}")
print(cost([20,20,30,80,6,10]))       


def cheap(l1):
    cheap = l1[0]
    for i in l1:
        if i < cheap:
            cheap = i
    return (f"cheap : {cheap}")
print(cheap([20,20,30,80,6,10]))  



"""fact using lambda"""
fact = lambda num : 1 if num <=1 else num * fact(num-1)
print(fact(5))




