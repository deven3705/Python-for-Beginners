# ***********************************Ex-2...ch3*********************************
"""input user name and age 
if name starts forn a or A and age is above 10
print you can watch coco mivie
else print 'sorry ,you cant watch'"""

# name=input('Enter your name : ')
# age=int(input('Enter your age : '))
# if age>10 and (name[0]=='a' or name[0]=='A'):
#     print('You can watch coco movie')
# else:
#     print('Sorry! You cant watch coco')


# ********************************if elif else statement*****************************

# age=int(input("Enter age : "))
# if 0<=age<=3:
#     print("Ticket price : FREE")
# elif 4<=age<=10:
#     print("Ticket price : 150/-")
# elif 11<=age<=60:
#     print("Ticket price : 250/-")
# else:
#     print("Ticket price : 200/-")


# ******************************** in keyword***************************************
# name="Deven"

# if 'd' in name:
#     print('d is present in name ')
# else:
#     print("not present")


# *******************************check empty or not*********************************
# name=""
# if name:                                     #true if string present
#     print("string is present")
# else:                                       #false if string is absent
#     print("string absent")

                       # use
# name=input("Enter your name : ")
# if name:
#     print(f"your name is {name}")
# else:
#     print("you didnt type anything")


# ********************************** while loop ***********************************
# i = 1
# while i<=10:
#     print("hello world")
#     i=i+1

# """sum of numbers"""
# #sum: 1 to 10 numbers
# sum=0
# i=1
# while i<=10:
#     sum=sum+i
#     i+=1
# print("sum 1-10 is :",sum)


# **********************************Ex-3...ch3**********************************
"""sum of n natural numbers"""

# n=int(input("enter number upto which to do sum : "))
# sum=0
# i=1
# while i<=n:
#     sum+=i
#     i+=1
# print("sum of n numbers :",sum)


# **********************************Ex-4....ch3*********************************
"""problem
ask user to input a number containing more than one digit
example 1256
calculate 1+2+5+6 and print

algorithm - (method to solve problem in human language)
ask input in string, i.e don't change string to int
example "1256"
pick string character one by one and change to int
int (example [0])+ int(example[1]) .... go upto len(example)-1"""

# 1)
# n=input("Enter number : ")
# sum=0
# for i in range(1,len(n)+1):
#     rem=int(n)%10                                   #by formula method
#     sum=sum+rem
#     n=int(n)//10
# print("sum of digits:",sum)

# 2)
# n=input("Enter number : ")
# sum=0
# i=0
# while i < len(n):                                 #by indexing method
#     sum=sum+int(n[i])
#     i+=1
# print(sum)


# ***********************************Ex-5....ch3**********************************
"""input user name and print count of each words
ex="deven "
d=1
e=2
v=1
n=1
 =1  """

# name=input("Enter name : ")

# temp_var=""
# i=0
# while i < len(name):
#     if name[i] not in temp_var:
#         temp_var+=name[i]
#         print(f"{name[i]} : {name.count(name[i])}")
#     i+=1


# **********************************infinite loop**********************************
""" Stop infinite loop --> ctrl+c """

# i=0
# while i<=10:
#     print("hello world")

# while True:
#     print("hello world")




