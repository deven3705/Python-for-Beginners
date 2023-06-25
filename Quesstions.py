"""slice index from 2 to 5 and print resulting sublist"""
# name="Python"
# print(name[2:5])                    #->tho

# print(name[0:6:2])
# print(name[1:6:2])

"""friuts dictionary with keys and value assigned to it,print resulting dict"""


"""append 8 and 9 in the list"""
# list_1=[1,2,3,4,5]
# list_2=8,9

# list_1.append(list_2)
# print(list_1)                     #-->[1, 2, 3, 4, 5, [8, 9]]



#string reverse
# name=input('enter your name : ')
# print(name[::-1])


# """fibonacci series"""
# def fibonacci(n):
#     a=0
#     b=1
#     if n==1:
#         print(a)

"""rev a number"""
# a = input("enter number: ")
# print(a[::-1])

def rev_no(n):
    temp = 0
    while(n != 0):
        r = n % 10
        temp = temp*10 + r
        n = n // 10
    return temp

a = int(input("enter number: "))
print(rev_no(a))



