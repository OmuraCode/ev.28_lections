# Задание 5
# Напишите код который сохраняет все названия категорий со страницы:

# https://enter.kg/

# в список category_list.

# После, напишите функцию которая имеет два параметра - список категорий - categories и ключевое слово - keyword.

# Функция должна производить поиск по ключевому слову в списке заголовков category_list и возвращать список заголовков которые содержат данное слово (независимо от регистра).

# К примеру:

# print(find_category(category_list, 'Ноутбуки')) 
# Вывод будет:

# ['Ноутбуки, Ультрабуки, Гот. решения (1281)', 'Ноутбуки (1235)', 'Ноутбуки, Ультрабуки, Гот. решения(1281)', 'Ноутбуки и ультрабуки']


from bs4 import BeautifulSoup
from requests import get

htnl = get('https://enter.kg/').text
soup = BeautifulSoup('html', 'html.parser')
container = soup.find('ul', class_='VMmenu')
category_list = [x.text for x in container.find_all('a')]
print(category_list)

def find_category(categories, keyword):
    return[x for x in categories if keyword.lower() in x.lower()]

print(find_category(category_list, 'Ноутбуки'))