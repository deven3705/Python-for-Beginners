n = int(input("enter total no of number to print fibonacci series :  "))
a,b=0,1
print(a,b)
for i in range(2,n):
    c = a+b
    print(c,end=" ")
    a=b
    b=c