""" dict comprehension """
# square ={1:1, 2:4, 3:9}

# square ={i:i**2 for i in range(1,5)}
# # print(square)                                            # {1: 1, 2: 4, 3: 9, 4: 16}

# for k,v in square.items():
#     print(f'{k} : {v}')

# string = 'deven'
# word_count = {char:string.count(char) for char in string}
# print(word_count)                                       # {'d': 1, 'e': 2, 'v': 1, 'n': 1}


#********************************************* if else **********************************************
# d= {1:'odd', 2:'even'}
# odd_even = {i:('odd' if i%2 != 0 else 'even') for i in range(1,7)}
# print(odd_even)


#******************************************************************************************************
""" sets comprehension """
# s = {k**2 for k in range(1,8)}
# print(s)                                 # {1, 4, 36, 9, 16, 49, 25}


# square={i:i**2 for i in range(10) if i%2 == 0}
# print(square)


# dict=range(10)
# print(dict)


# dict=[i for i in range(0,10)]
# l1=[]
# for i in dict:
#     l1.append(i**2)
# print(l1)







