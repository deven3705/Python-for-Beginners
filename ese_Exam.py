# res = [10,20,30,10,60,90,30,50,20]

# li = {}
# for i in res:
#     if i not in li:
#         li[i] = 1
#     else:
#         li[i] +=1
# print(li)


# li = ['fox','small','redy','red','yash']
# length = len(li)
# mid = length//2

# #before mid
# print(li[0:mid])
# #after mid
# print(li[mid:length+1])


# yourTuple = ('yash','deven','cherey','yellow','send')
# a,b,*c = yourTuple
# print(c)


# mywallet = {}
# mywallet['ccard']=1
# mywallet['vcard']=4
# mywallet['yash']=1

# mywallet['yash']=mywallet.get('yash',0)+1
# print(mywallet)

# del mywallet['ccard']
# print(mywallet)

# a = dict(sorted(mywallet.items()))
# print(a)

# b = dict(sorted(mywallet.items(),key=lambda ele:ele[1]))
# print(b)


# import math
# a=int(input("Enter the number :"))
# print("""1.Square roo
# 2.Cube root""")
# choice=int(input("Enter your choice :"))
# match choice:
#     case 1:
#         ans=math.sqrt(a)
#         print("Square root is",ans)
#     case 2:
#         sol=math.cbrt(a)
#         print("Cube root is ",sol)
#     case _:
#         print("Select appropriate option..!")

# n = input("enter number : ")
# rev_n = n[::-1]
# if n==rev_n:
#     print("palindrome")


# n = int(input("enter total no of number to print fibonacci series :  "))
# a,b=0,1
# print(a,b,end = " ")
# for i in range(2,n):
#     c = a+b
#     print(c,end=" ")
#     a,b=b,c

import numpy as np
arr = np.array([1,2,3,4])
print(arr)
