# name="python is a programming language"
# # name=name.upper()
# # name=name.replace("python","c")
# print(name.replace("python","c"))
# print(f"upper case of pthon is {name.capitalize()}")


# cube=[i**3 for i in range(1,6)]
# print(cube)


# def cube(l1):
#     l2=[]
#     for i in l1:
#          l2.append(i**3)
#     print(l2)

# cube([1,2,3,4,5])


# n=int(input("enter power : "))
# def cub(n,*a):
#     return [i**n for i in a]

# # li=[1,2,3,4,5]
# print(cub(n,*[1,2,3,4,5]))





# class info:
#     def __init__(self,name,roll):
#         self.name = name
#         self.roll = roll

#     def asd(self):
#         f = open("new.txt","a") 
#         for i in range(1,4):
#             f.write(f"name : {self.name}")
#             f.write(f"roll : {self.roll}")
#         f.close()

# for i in range(1,4):
#     a= input("enter name : ")
#     b = int(input("enter roll: "))
    
# t = info(a,b)
# print(t.asd)




n=int(input("Enter the number :"))
for i in range(2,n):
    if n % i == 0:
        print(f"{n} is not a prime number..!")
        break
else:
    print(f"{n} is prime number..!")








