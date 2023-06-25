""" it  is used when we have pass more argument in function """
# def total(a,b):
#     return a+b
# print(total(2,3))                     # -> will take only 2 values not more than 2 values 

# def all_total(*args):
#     sum=0
#     for i in args:
#         sum += i
#     return sum

# print(all_total(1,3,4,7,2))

#******************************************* args with normal parameters ***************************************
# def mult_nums(num, *args):
#     multiply = 1
#     for i in args:
#         multiply *= i
#     return multiply

# print(mult_nums(3,2,4))                              # 4*2=8 and  3 will not be considered it will assign to num


#******************************************* *args as argument ****************************************8
# def mult_nums( *args):
#     multiply = 1
#     for i in args:
#         multiply *= i
#     return multiply

# nums = [2,3,4]
# print(mult_nums(*nums))                            #-> 24


#********************************************* Ex 1 ch-11***********************************************
"""def a function
num=[1,2,3]   to_power(3,*num)

output --> 
list [1,8,27]"""

# def power(num,*args):
#     if args:
#         return [i**num for i in args]
#     else:
#         return "you didn't pass any args"
    
# li = [1,4,2]
# print(power(3,*[]))


"""******************************************* kwargs *********************************************"""
# def func(**kwargs):
#     for k,v in kwargs.items():
#         print(f"{k} : {v}")

# d = {'name':'deven', 'age':20}
# func(f_name = 'deven', l_name = 'patel')
# func(**d)


#******************************************** parameter order ***************************************
# def func(name,*args,l_name='unknown',**kwargs):
#     print(name)
#     print(args)
#     print(l_name)
#     print(kwargs) 

# func('deven',1,2,3,4, a=1,b=2)


#********************************************** Ex 2 ****************************************************
"""func
list, reverse_str = true
list """

# def func(l,**kwargs):
#     if kwargs.get('reverse_str') == True:
#         return [name[::-1].title() for name in l]
#     else:
#         return [name.title() for name in l]
    
# names = ['abc','cdh']
# print(func(names))
# print(func(names, reverse_str = True))



