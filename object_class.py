# class subcriber:
#     def __init__(self,name,age,email_id,mobile_no):
#         self.name = name
#         self.age = age
#         self.email = email_id
#         self.number = mobile_no
    

# var = subcriber("deven", 20, "devenpatel987@gmail.com", 8378040004)
# print(var.name)

# --------------------------------------------------------------------------------------------------

# class naro:
#     def __init__(self,data):
#         self.name,self.age,self.email_id,self.mobile_no = data

# var = naro(("deven", 20, "devenpatel987@gmail.com", 8378040004))
# print(var.name)
# print(var.mobile_no)

# ----------------------------------------------------------------------------------------------------

# class animals:
#     def __init__(self,name,category):
#         self.name = name
#         self.category = category

#     def body_data(self,nol,noT,noe,non,nom):
#         self.no_of_legs = nol
#         self.no_of_tail = noT
#         self.no_of_eyes = noe
#         self.no_of_nose = non
#         self.no_of_mouth = nom

#     def print_body_data(self):
#         print("The ", self.name, "has ", self.no_of_legs," number of legs")
#         print("The ", self.name, "has ", self.no_of_tail," number of tail")
#         print("The ", self.name, "has ", self.no_of_eyes," number of eyes")
#         print("The ", self.name, "has ", self.no_of_nose," number of nose")
#         print("The ", self.name, "has ", self.no_of_mouth," number of mouth")

# p = animals("bobby","cat")

# ------------------------------------------------------------------------------------------------------

# class students:
#     def __init__(self,name,age,rollno):
#         self.name=name
#         self.age=age
#         self.rollno=rollno

# shiv = ("shiv",19,63)
# dven = ("deven",37,84)

# for i in [shiv,dven]:
#     print(i.name)

# -----------------------------------------------------------------------------------------------------
"""area of rectangle"""
# class rect:
#     def __init__(self,l,b):
#         self.l = l
#         self.b = b

#     def print(self):
#         print
# p = rect(3,4)
# print(p.l*p.b)

# ----------------------------------------------------------------------------------------------------------

# class rect:
#     def __init__(self,l,b):
#         self.l = l
#         self.b = b

#     def area(self):
#         return self.l * self.b

# a=float(input("enter length: "))
# b= float(input("enter breadth: "))

# p = rect(a,b)
# print(p.area())

# -------------------------------------------------------------------------------------------------------------

# class obj:
#     def __init__(self,shape,l,b):
#         self.shape=shape
#         self.l = l
#         self.b = b

#     def shapecal(self):
#         if self.shape == "triangle":
#             return 0.5 * self.l * self.b
#         elif self.shape == "rectangle":
#             return self.l * self.b
#         else:
#             print("i dont know area of shape you entered")


# a=float(input("enter length: "))
# b= float(input("enter breadth: "))
# s= input("enter shape: ")

# p=obj(s,a,b)
# print(f"Area of {s}: ",p.shapecal())

# -------------------------------------------------------------------------------------------------------

# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance
        
#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Rs.{amount} has been deposited in your account.")
    
#     def withdraw(self, amount):
#         if amount > self.balance: 
#             print(f"cannot be withdrawn,only {self.balance} can be withdrawn ")
#         else:
#             self.balance -= amount
#             print(f"Rs.{amount} has been withdrawn from your account.")
        
#     def print_balance(self):
#         print(f"balance : Rs.{self.balance}")
        

# start = BankAccount(2000)
# start.deposit(4000)
# start.deposit(3784)
# start.withdraw(5287)
# start.withdraw(4498)

# start.print_balance()

# -------------------------------------------------------------------------------------------------------
import time

def time(func):
     def modify(*args,**kwargs):
          start = time.time()
          a = func(*args,**kwargs)
          end = time.time()
          time_require = end - start
          print(f"required time is:{time_require}")
          return a
     return modify

@time
def recur_factorial(n):
    if n == 1:
        return n
    elif n < 1:
         return ("NA")
    else:
         return n * recur_factorial(n-1)
    
print (recur_factorial(5))

