from  bs4 import BeautifulSoup
import requests
import csv

def get_html(url: str) -> str:
    '''Получает html разметку определенного сайта по url'''
    response = requests.get(url)
    return response.text

def get_soup(html: str) ->BeautifulSoup:
    '''Наша функция получает html разметку и структурирует ее в bs'''
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def get_last_page(soup:BeautifulSoup) ->int:
    '''Функция которая возвращает последнюю страницу на сайте'''
    pages = soup.find('ul', class_='pagination').find_all('a', class_='page-link')
    last_page = pages[-1].get('data-page')
    return int(last_page)

def get_data(soup: BeautifulSoup)-> list:
    '''Получает нужные данные с сайта машина.кг и возвращает в виде списка'''
    container = soup.find('div', class_='table-view-list')
    cars = container.find_all('div', class_='list-item')
    result = []
    for car in cars:
        name = car.find('h2', class_='name').text.strip()
        try:
            img = car.find('img', class_='lazy-image').get('data-src')
        except:
            img = 'No Image'
        price_div = car.find('div', class_='block price')
        price = price_div.find('p').find('strong').text
        # desc1 = car.find('p', class_='year-miles').text.strip()
        # desc2 = car.find('p', class_='body-type').text.strip()
        # desc3 = car.find('p', class_='volume').text.strip()
        # description = f'{desc1} {desc2} {desc3}'
        ls = ['year-miles', 'body-type', 'volume']
        desc = ', '.join(car.find('p', class_=x).text.strip() for x in ls)
        data = {
            'name': name, 'desc': desc, 'price': price, 'img': img
        }
        result.append(data)
    return result

def prepare_csv() -> None:
    '''Функция которая подготавливает cvs файл'''
    with open('cars.csv', 'w') as file:
        fieldnames = ['№', 'Name', 'Description', 'Price', 'Image URL']
        writer = csv.DictWriter(file, fieldnames)
        writer.writerow({
            '№': '№',
            'Name': 'Name',
            'Description': 'Description',
            'Price': 'Price',
            'Image URL': 'Image'
        })

count = 1
def write_to_csv(data: list) -> None:
    '''Записывает все данные в csv файл'''
    with open('cars.csv', 'a') as file:
        fieldnames = ['№', 'Name', 'Description', 'Price', 'Image URL']
        writer = csv.DictWriter(file, fieldnames)
        global count
        for car in data:
            writer.writerow({
                '№': count,
                'Name': car['name'],
                'Description': car['desc'],
                'Price': car['price'],
                'Image URL': car['img']
            })
            count += 1
            
def main():
    i=1
    prepare_csv()
    while True:
        url = 'https://www.mashina.kg/search/all={i}'
        html = get_html(url)
        soup = get_soup(html)
        last_page = get_last_page(soup)
        data = get_data(soup)
        # print(data)
        write_to_csv(data)
        print(f'Спарсили {i}/{last_page} страницу')
        print()
        if i == 13:
            break
        i += 1

main()
