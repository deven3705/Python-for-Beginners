#******************************************for() loop*********************************
# for i in range(1,10):                       #1-9 times ....it excludes 10
#     print(f"hello world {i}")

"""sum 1-10"""
# total=0
# for i in range(1,11):
#     total+=i
# print(total)                              #55

"""sum of digits"""
# total=0
# n=input("ENter number : ")
# for i in range(0,len(n)):
#     total+= int(n[i])
# print(total)

"""user name and count each char"""
# name=input("enter your name : ")
# temp=""
# for i in range(0,len(name)):
#     if name[i] not in temp:
#         print(f"{name[i]}: {name.count(name[i])}")
#         temp+=name[i]


#************************************Break and Continue*********************************
# for i in range(1,11):
#     if i == 5:
#         break  
#     print(i)                                 #1 2 3 4

# for i in range(1,11):
#     if i == 5:
#         continue
#     print(i)                                 #1 2 3 4 6 7 8 9 10


#********************************Exercise**********************************
"""number guessing game"""
# import random
# number = int (input("Guess number b/w 1 and 100 : "))
# winning_number = random.randint(1,100)
# guess = 1

# while True:
#     if number == winning_number:
#         print(f"you win! , and you guessed this number in {guess} times")
#         break
#     else:
#         if number < winning_number:
#             print("too low")
        
#         else:
#             print("too high")
#         guess+=1
#         number=int(input("guess again : "))


#********************************step arg in range*********************************
# for i in range(1,11,2):
#     print(i)                              #1 3 5 7 9

# for i in range(10,0,-1):     
#     print(i)                               #10 9 8 7......2 1



#*******************************for loop strings************************************
# name='deven'
# for i in range(len(name)):
#     print(name[i])                        #d e v e n

# for i in name:
#     print(i)                                #d e v e n

"""sum of digits"""
# num=input("Enter number : ")
# total=0
# for i in num:
#     total+=int(i)
# print(total)



