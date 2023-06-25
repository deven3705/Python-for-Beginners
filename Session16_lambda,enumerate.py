#*********************************************** lambda expression***************************************
# def add(a,b):
#     return a+b

# add2 = lambda a,b : a+b
# print(add2(2,3))

# mult = lambda a,b : a*b
# print(mult(3,4))


#***************************************** practise ******************************************
# def is_even(a):
#     return a%2 == 0 

# print(is_even(5))

# iseven2 = lambda a: a%2==0
# print(iseven2(6))

# last_char = lambda s : s[-1]
# print(last_char('deven'))

"""************************************* lambda if else *********************************"""
# func = lambda s : True if len(s) > 5 else False
# print(func('devenp'))                                     # True
#                                    #or
# func = lambda s : len(s) > 5 
# print(func('devenp'))                                     # True

fact = lambda num : 1 if num <=1 else num * fact(num-1)
print(fact(5))



















