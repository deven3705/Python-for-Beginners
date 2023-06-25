#***************************************Functions Intro************************************
# def add_two(a,b):
#     return a+b

# print(add_two(1,7))

# a=int(input("Enter first number : "))
# b=int(input("Enter second number : "))
# print(add_two(a,b))

# f_name=input("Enter first name : ")
# l_name=input("Enter second name : ")
# print(add_two(f_name,l_name))


#***********************************print v/s return**********************************
# def add_three(a,b,c):
#     print (a+b+c)

# add_three(5,5,5)


#**********************************func. practice************************************
# def last_char(name):
#     return name[-1]
# print(last_char("deven"))                          #n

# def odd_even(num):
#     if num%2 == 0:
#         return 'even'
#     return 'odd'
# print(odd_even(10))

# def is_even(num):
#     if num%2 == 0:
#         return True
#     return False
# print(is_even(9))

# def is_even(num):
#     return num%2 == 0
# print(is_even(8))

# def song():
#     return 'happy birthday'
# print(song())


#***************************************Ch4....Ex-1*********************************
"""define function ,take two input numbers return greater num"""
# def great(a,b):
#     if a > b:
#         return a
#     return b

# num1 = int(input("ENter first num : "))
# num2 = int(input("ENter second num : "))
# big=great(num1,num2)
# print(f'{big} is greater')


#***************************************greatest************************************
# def greatest(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>c:
#         return b
#     else:
#         return c

# num1,num2,num3=input("Enter three numbers : ").split()
# big=greatest(num1,num2,num3)
# print(f"{big} is greater")


#***********************************func inside func*****************************
# def greater(a,b):
#     if a > b:
#         return a
#     return b

# def greatest(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>c:
#         return b
#     else:
#         return c
    
# def new_great(a,b,c):
#     bigger = greater(a,b)
#     return greater(bigger,c)
# print(new_great(100,499,78))


#************************************Ch4...Ex-2*********************************
"""define is_palindrome func ,takes input one word and return true --> palindrome else false"""
# def is_palindrome(string):
#     rev=string[::-1]
#     if string == rev:
#         return 'palindrome'
#     return 'not palindrome'

# string=input('Enter string : ')
# print(is_palindrome(string))


#**********************************fibonacci series*****************************
# 0 1 1 2 3 5 8 13 21...

# def fibonacci(n):
#     a=0     #1 number
#     b=1     #2 number
#     if n == 1:
#         print(a)
#     elif n == 2:
#         print(a, b)       #0 1
#     else:
#         print(a,b, end=" ")
#         for i in range(n-2):
#             c=a+b
#             print(c ,end=" ")
#             a=b
#             b=c

# fibonacci(5)




