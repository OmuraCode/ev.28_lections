# dict() - словарь - упорядоченная коллекция элементов (Python 3.7 -> ordered). кадлый элемент внутри словаря 
# хранится в виде пары --> (ключ; значение)

# ассоциативный массивб hash table, object(js), structure == dictionary.py

# ключами могут быть только изменяемые типы данных и в словаре сохраняются только уникальные ключи.
# тогда как значениями могут выступать любые типы данных.


# thisdict = {
#     'brand': 'Ford',
#     'model': 'Mustang',
#     'year': 1967
# }
# print(thisdict)
# print(type(thisdict))
# print(thisdict ['brand'] , thisdict['model'])
# print(thisdict[ 'year'])

# thisdict['motor'] = 'GTE Turbo'
# thisdict['brand'] = 'Tesla' # перезапись
# print(thisdict)

# ____________

# Способы объявления

# a = {}
# b = dict()

# _________________________________
# Методы словарей
# print(dir(dict))

# items, keys, values


# user_info = {
#     'first_name':'John',
#     'last_name': 'Snow',
#     'age': 24,
#     'email': 'johnsnow@gmail.com', 
#     'role': "admin",
# }
# ls = user_info.keys()
# ls = list (ls)
# print(ls[2:])




# user_info = {
#     'first_name':'John',
#     'last_name': 'Snow',
#     'age': 24,
#     'email': 'johnsnow@gmail.com', 
#     'role': "admin",
# }

# ls = list(user_info.values())
# print(ls)




# user_info = {
#     'first_name':'John',
#     'lsat_name': 'Sm=now',
#     'age': 24,
#     'email': 'johnsnow@gmail.com', 
#     'role': "admin",
# }

# items = user_info.items()
# print(items)

# print(user_info)
# for value  in user_info.values():
#     print(value)




# user_info = {
#     'first_name':'John',
#     'lsat_name': 'Sm=now',
#     'age': 24,
#     'email': 'johnsnow@gmail.com', 
#     'role': "admin",
# }
# for key in user_info.keys():
#     print(key) 


# for key, value in user_info.items():
#     print(f'keys: {key}, values: {value}')



# Изменение 

# dict_ = {'name': 'Jack', 'age': 17}
# print(dict_)
# dict_['name'] = 'John'
# dict_['age'] = 24
# dict_['adress'] = 'Winterfell'
# print(dict_)
# dict_.update({'age': 25, 'adress': 'BlackCastle'})
# print(dict_)

# _____________________________

# Получение данных со словаря - 
# get()

# dict_ = {1: 'Pizza', 2: 'Burger', 3: 'Steak'}
# print(dict_[2], '!!!')
# print(dict_.get(1))


# setdefault - работает так же как get, но если нет такого ключа, то создает новую пару из этого ключа

# dict_ = {1: 'Pizza', 2: 'Burger', 3: 'Steak'}
# print(dict_.setdefault(4, 'Manty'))
# print(dict_)


# ------------------------------
# Создание словаря - fromkeys

# ls = list(range (1, 100))
# new_dict = dict.fromkeys(ls, 'value')
# print(new_dict)


# ________________________________
# удаление элементов
# pop, popitem

# pop(<key>) - удаляет пару по ключу

# dict_ = {'name': 'John', 'last_name': 'Snow'}
# print(dict_)
# removed = dict_.pop('last_name')
# print(dict_)
# print(removed)



# popitem - удаляет последнюю пару
# dict_ = {'name': 'John', 'last_name': 'Snow'}
# removed = dict_.popitem()
# print(dict_)
# print(removed)

# ______________________________________
# МАГАЗИН


# roles = {
#     0:'Admin',
#     1: 'Customer',
#     2: 'Vendor',
# }

# users = {
#     1: {
#     'id': 1, 'role': roles[2], 'username': 'Tirion',
#     },
#     2: {
#     'id': 2, 'role': roles[0], 'username': 'John',
#     },
#     3:{
#     'id': 3, 'role': roles[1], 'username': 'Raychal',
#     }
# }
# 3
# print(users)


# product = {
#     'id': 1, 
#     'title': 'Samsung Galaxy A51',
#     'description': 'Lorem Ipsum',
#     'price': 250
# }
# print(product)

# id_user = int(input('VVedite id: '))
# if users[id_user]['role'] == roles[0]:
#     product['description'] = input('Vvedite opisaniye: ')
# else:
#     print('You do not have permissions!')

# print(product)




