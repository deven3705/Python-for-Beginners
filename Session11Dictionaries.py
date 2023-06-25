"""d={"key":"apple","a":23,"b":[1,2,4,6,7],"c":{"key":"orange","b":5}}

print(d['c']["b"])"""

#**************************************** intro *******************************
# user = {'name' : 'deven', 'age' : 20}
# print(user['name'])                             #deven

"""second method to create dict"""
# user1 = dict(name = 'deven', age = 20)
# print(user1)                                     #{'name': 'deven', 'age': 20}


# user_info = {
#     'name' : 'deven',
#     "age" : 20,
#     'fav_movies' : ['coco', 'deven', 'dhoom'],
#     'fav_tunes' : ['awakening','fairy atle']
# }
# print(user_info['fav_movies'])


"""add data to empty dict"""
# user_info = {}
# user_info['name'] = 'decen'
# user_info['age'] = 20
# print(user_info)                                    #{'name': 'decen', 'age': 20}


#*************************************** looping and in keyword ****************************************
# user_info = {
#     'name' : 'deven',
#     "age" : 20,
#     'fav_movies' : ['coco', 'deven', 'dhoom'],
#     'fav_tunes' : ['awakening','fairy atle']
# }

"""check for key exist"""
# if 'name' in user_info:
#     print('present')
# else:
#     print('not present')

"""check for value exist"""
# if 20 in user_info.values():
#     print('present')
# else:
#     print('not present')

""" loops """
# for i in user_info:                                
#     print(i,end=" ")                                  # name age fav_movies fav_tunes

# for i in user_info:
#     print(user_info[i],end=" ")                      # deven 20 ['coco', 'deven', 'dhoom'] ['awakening', 'fairy atle'] 

# for i in user_info.values():                                
#     print(i,end=" ")                             # deven 20 ['coco', 'deven', 'dhoom'] ['awakening', 'fairy atle']


""" item method """
# user_items = user_info.items()
# print(user_items)


# for key,value in user_info.items():
#     print(f"key is {key} and value is {value}")


#*********************************** add , delete data *****************************************
# user_info = {
#     'name' : 'deven',
#     "age" : 20,
#     'fav_movies' : ['coco', 'deven', 'dhoom'],
#     'fav_tunes' : ['awakening','fairy atle']
# }

""" add data """
# user_info['fav_songs'] = 'rafta'
# print(user_info)

"""pop method """
# user_info.pop('fav_tunes')
# print(user_info)

""" popitem method """
# popped_item = user_info.popitem()
# print(popped_item)
# print(user_info)

#*************************************** update dict ******************************************
# user_info = {
#     'name' : 'deven',
#     "age" : 20,
#     'fav_movies' : ['coco', 'deven', 'dhoom'],
#     'fav_tunes' : ['awakening','fairy atle']
# }

# more_info = {'state' : 'delhi', 'hobbies' : ['coding', 'reading', 'guitar']}

# user_info.update(more_info)
# print(user_info)


#********************************** fromkeys,get,clear,copy method *********************************
""" 1) fromkeys method""" 
# d = {'name' : 'sgfdih', 'age' : 20}

# # d = dict.fromkeys(['name','age','height'],'deven')
# # print(d)                                             # {'name': 'deven', 'age': 'deven', 'height': 'deven'}

# d = dict.fromkeys(['name','age','height'],['deven','patel'])
# print(d)                             # -->> assigns list to all..name,age,height


""" 2) get method """
# d = {'name' : 'unknown', 'age' : 'unknown'}
# # print(d['names'])                          # --> key error
# print(d.get('names'))                       # --> None

# if d.get('name'):
#     print('present')
# else:
#     print('absent')


#************************************ more about get() ************************************
# user = {'name' : 'deven', 'age' : 20, 'age' : 39}
# print(user.get('fav', 'nhi ahe'))
# print(user)                                       # {'name': 'deven', 'age': 39}


#**************************************** Ex 1 *****************************************
""" cube finder in dict """
# def cube(n):
#     cubes = {}
#     for i in range(1,n+1):
#         cubes[i] = i**3
#     return cubes

# print(cube(5))                                # {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}


#****************************************** word counter *****************************************  
# def word_counter(s):
#     dict = {}
#     for char in s:
#         dict[char] = s.count(char)
#     return dict

# print(word_counter('deven'))                           # {'d': 1, 'e': 2, 'v': 1, 'n': 1}


#***************************************** Ex 2 ***********************************************
"""user input and store info in dictionary as per given format"""
# user_info = {
#     'name' : 'deven',
#     "age" : 20,
#     'fav_movies' : ['coco', 'dhoom'],
#     'fav_songs' : ['awakening', 'fairy atle']
# }


user = {}
name = input('enter your name : ')
age = input('enter your age : ')
fav_movies = input('enter fav movies separated by comma : ').split(',')
fav_songs = input('enter fav songs separated by comma : ').split(',')

user['name'] = name
user['age'] = age
user['fav_movies'] = fav_movies
user['fav_songs'] = fav_songs
# print(user)

for key,value in user.items():
    print(f"{key} : {value}")













































