#***********************************center method******************************
# name='deven'
# #-->**deven**                            #=to add stars to both side
# print(name.center(9,"*") )                   # string len + stars[5+4(2r+2l)=9]
# print(name.center(8,"*") )                 #-->*deven**   = adds to right side

# name=input('enter your name : ')
# print(name.center(len(name)+8,"*"))


#*********************************strings are immutable**************************
# immutable=if we have assigned value string to var ,we cannot change it later

# string='string'
# # print(string[1])                         #-->t
# # string[1] ='T'                         # this is wrong....this cannot replace

# print(string.replace('t','T'))          #->sTring
# print(string)                          #->string....it will not replace the new string
                                       #it doesnt make change in old string


# ******************************Assignment operators**********************************
# name='dev'
# name += "en"
# print(name)                         #->deven


#*********************************if else statement*************************************
# age=int(input('Enter your age : '))

# if age >18 :
#     print('Eligible for voting')
# else:
#     print('Not Eligible')


#********************************* NUMBER GUESSING GAME**************************************
"""EXERCISE, NUMBER GUESSING GAME
# Make a variable, like winning number and assign any number to it.
# Ask user to guess a number .
# if user guessed correctly then print "YOU WIN !!!!"
# if user didn't guessed correctly then:
    # if user guessed lower than actual number then print "too low"
    # if user guessed higher than actual number then print "too high"
# bonus
#google "how to generate random number in python " to generate random
#winning number"""

import random
choice=int(input('guess a number from list [2,6,9,5,11,34]: '))
ran=random.choice([2,6,9,5,11,34])
print('Your entered no = ',choice)
print("random number= ",ran)

if choice == ran:
    print('YOU WIN !!!')
else:
    print('YOU LOST !!!')


#**********************************AND OR operators***************************************
# name='xyz'
# age=20
# if name =='xyz' and age ==20:
#     print('true')
# else:
#     print('false')

# if name =='abxyz' or age ==20:
#     print('true')
# else:
#     print('false')

