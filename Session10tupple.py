#looping in tuples
#tuple with one element
# tuple without parenthesis
# tuple unpacking
# list inside tuple some functions that you can use with tuple

#**************************************** loop in tuple ****************************************
# mixed = (1,2,3,4.0)
# for i in mixed:
#     print(i)


#************************************* tuple with one element**********************************
# nums = (1,)
# print(type(nums))


#************************************ tuple without parenthesis *******************************
# guitars = 'yamaha', 'baton rouge', 'taylor'
# print(type(guitars))


#************************************* tuple unpacking ****************************************
# guitarists = ('maneli jamal', 'eddie van der meer', 'andrew foy')
# guitarists1,guitarists2,guitarists3 = guitarists
# print(guitarists1)


#************************************* list inside tuple *************************************
# fav = ('southern mangolia', ['tokyo theme', 'landscape'])

# fav[1].pop()                    #('southern mangolia', ['tokyo theme'])
# fav[1].append('we made it')     #('southern mangolia', ['tokyo theme', 'we made it'])  --> landscape gets pop then str is added
# print(fav)


#********************************** func returning two values **********************************
# def func(int1, int2):
#     add = int1 + int2
#     multiply = int1 * int2
#     return add, multiply

# print(func(2,4))                                                  #(6, 8)

# add, multiply = func(2,4)
# print(f"addition={add}\nmultiplication={multiply}")              # addition=6
                                                                 # multiplication=8


#************************************ more about tuple **********************************************
# nums = tuple(range(1,11))
# nums = list((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))                                #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(nums)
 


