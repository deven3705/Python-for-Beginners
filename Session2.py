# +   -> addition
# -   -> subtraction
# *   -> multiplication
# /   -> float division   -->4/2=2  -->2/4=0.5
# //  -> integer division -->4//2=2  -->2//4=0
# %   -> remainder
# **  -> exponent         -->print(2**3)=2^3=8


# print(2+3)                       # -->5
# print(int(4/2))                   # -->2
# print(4/2)                        # -->2.0
# print(4//2)                        #-->2

# print(2**0.5)                     #--> 0.5 =sq. root
# print(round(2**0.5,4))


# Precedence Rule 
# 1)parenthese -->highest
# 2)exponent   -->l to r
# 3)*,/,//,%,+,-  -->l to r

# print((2+3)*5/2%6)       #5*5/2%6
#                          #25/2%6
#                          #12.5%6 =0.5

# print(2**3**2)          #(2**9)


#************************variables******************************
# name='deven'
# print(name)
# print("deven")



#***********************string concate**************************
# f_name='deven '
# l_name='patel'
# full_name=f_name+l_name
# print(full_name)
# print(f_name+l_name)

# # print(f_name+3)                #error=string+int
# print(f_name+"3")              #deven 3
# print(f_name+str(3))           #deven 3
# print(f_name*3)                #deven deven deven


#************************user input*******************************
# name=input('type ur name = ')
# print("hello " + name)
# age=input('enter age ?')                    #input will take in string
# print('your age is '+age)          
# # ......->your age is 20                  #it concates bcoz input func. takes as string(whether be it number )



#*********************int() func.**********************************
# n_1=int(input('enter fisrt name '))
# n_2=int(input('enter second name '))
# print(n_1+n_2)


#************************more var*********************************
# name,age="deven ","20"
# print("hello "+name+"your age is " +age)


#*******************more input in one line*************************
# name,age=input("enter name and age  ").split()
# print(name)
# print(age)

#or

# name,age=input("enter name  and age separate by comma ").split(",") 
# print(name) 
# print(age)


# print("pune","india")                 #pune india

# a=2
# b=3
# print(f"sum of {a} and {b} is {a+b}")
