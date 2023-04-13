# JSON - JavaScript Object Notation
# JSON - это единый текстовый формат данных, был создан для хранения и передачи данных между сервисами

# <filename>.json файл в формате JSON

# {
#     "id":1,
#     "author":{
#         "name" : "Ed Seeran",
#         "age": 35
#     },
#     "title": "don't",
#     "feat": false
# } --- это JSON 


# !!!!
# js object = {key: value}
# Py dict = {key: value}
# JSON = {key: value}


# Процессы сериалиэации и десериализации данных(конвертация)

# Cериалиэация (запись данных в JSON)- это перевод из Python в JSON формат
# dump - записывает данные в файл формата JSON
# dumps - записывает данные в текст формата JSON


# Десериализации (чтение данных из JSON) - это процесс перевода данных из JSON в PY dict
# load - функция которая считывает данные из файла JSON
# loads - функция которая считывает данные из текста JSON


# ---------------------
# Процесс сериализации

# import json

# dict_ = {
#     'name': 'John Snow',
#     'age': 24,
#     'status': True,
#     'wife': False,
#     'children': None
# }

# print(dict_, type(dict_))

# json_text = json.dumps(dict_)
# print
# print (json_text, type(json_text))




# 2 primer

# import json

# dict_ = {
#     'name': 'John Snow',
#     'age': 24,
#     'status': True,
#     'wife': False,
#     'children': None
# }

# print(dict_, type(dict_))

# with open ('new.json', 'w') as file:
#     json.dump(dict_, file, indent=4)

# print(dict_, type(dict_))
# 


# ---------------------
# Процесс сериализации

# import json

# with open('new.json', 'r') as file:
#     json_data = file.read()

# print (json_data, type(json_data))
# dict_ = json.loads(json_data)
# print()
# print(dict_, type(dict_))




# import json

# with open('new.json', 'r') as file:
#     dict_ = json.load(file)
#     print(dict_, type(dict_))







from urllib.request import urlopen
import json
import pprint as pp

url = 'https://randomuser.me/api/'
json_data = urlopen(url)
# print(json_data, type(json_data))

dict_ = json.load(json_data)
pp.pprint(dict_)