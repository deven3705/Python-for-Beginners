def fact(n):
    if n==1:
        return n
    elif n<1:
        print("not defined")
    else:
        f=1
        for i in range(1,n+1):
            f=f*i
        return f
        
print(fact(5))