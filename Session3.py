#**********************string format************************
# name="deven"
# age=24

# print("hello {} your age is {}".format(name,age))             #python3

# print(f"hello {name} your age is {age}")                      #py3.6

#**************************exercise 1****************************
"""1)aks user to input 3 numbers  and print average of that numbers using string formatting
  by string formtting , also by one print statement input"""

# a=int(input("enter first number ="))
# b=int(input("enter second number ="))
# c=int(input("enter third number ="))

# a,b,c=input("Enter three numbers comma separated=").split(",")

# print(f"Average of three numbers :{(int(a) + int(b) + int(c)) / 3}")


# **************************string indexing*************************
# language="python"

# p=0 ,-6
# y=1 ,-5
# t=2 ,-4
# h=3 ,-3
# o=4 ,-2
# n=5 ,-1
# print(language[2])                      # -->t
# print(language[-1])                     #-->n

# # ************************string slicing*****************************
# lang="python"
# #syntax -> [start arg : stop arg +1]

# print(lang[:2])                         #->py


# ***************************step arg***************************
# lang="python"
# syntax-[start arg : stop arg +1 : step]

# print("deven"[2:5])              #->ven
# print("deven"[0:5:1])            #->deven
# print("deven"[0:5:2])            #->dvn  increment by +1
# print("deven"[-1::-1])            #neved
# print("deven"[4:0:-1])           #neve


# ***************************Exercise 2****************************
# Q)ask user to input name and print in rev order
#   try to make in 2 line

# name=input("Enter ur name : ")
# print(f"reverse of {name} is {name[::-1]}")
#           #or
# name=input("Enter ur name : ")      
# rev=name[::-1]
# print(f"reverse of name is {rev}")


# ****************************string methods*******************************
# name="DeVen PaTel"


# # 1. len() function
# print(len(name))                    #->11

# # 2. lower() method
# print(name.lower())                 #deven patel

# # 3. upper() method
# print(name.upper())                #DEVEN PATEL

# # 4. title() method
# print(name.title())                #Deven Patel

# # 5. count() method
# print(name.count("e"))              #3



# ********************************Exercise 3*******************************
#take two comma separated input 
# 1- user name,ex-"DEven"
# 2- single char,"e"

# output-->
# 1) user name length
# 2) count the char that user inputed (case insensitive)


# name,char=input("enter comma sep. name and char :").split(",")
# print(f"length of name is {len(name)}")
# print(f"char count : {name.lower().count(char)}")


#****************************str method with spaces ->strip method******************
# name="     deven   "
# dots="............"
# #  strip() method
# print(name.lstrip() + dots)
# print(name.rstrip() + dots)
# print(name.strip()+ dots)                           #deven.............



# *******************************replace find method***********************
# 1. replace() method
# 2. find() method

# str="she is beautiful and she is good dancer"
# print(str.replace(" is "," was "))                  #--> both is will replce
# print(str.replace(" is "," was ",1))                #--> 1- only first is will replace



# print(str.find("is"))                              #->4
# print(str.find("is",8))                            # to find 2nd  is .........pahile is cha index no ch nntr cha index taka
#         #  or   --> if we dont know indice of first is
# is_pos1=str.find("is",1)                         
# is_pos2=str.find("is",is_pos1+1)
# print(is_pos2)                                         #-->25



 