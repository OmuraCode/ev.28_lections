from  bs4 import BeautifulSoup
import requests
import csv
# import urllib

response = requests.get('https://www.mashina.kg/motosearch/all/').text

def get_soup(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def get_data(soup):
    container = soup.find('div', class_='table-view-list')
    motoes = container.find_all('div', class_='list-item')
    result = []
    for moto in motoes:
        name = moto.find('h2', class_='name').text.strip()
        try:
            img = moto.find('img', class_='lazy-image').get('data-src')
        except:
            img = 'No Image'
        price_div = moto.find('div', class_='block price')
        price = price_div.find('p').find('strong').text
        desc1 = moto.find('p', class_='year-miles').text.strip()
        desc2 = moto.find('p', class_='body-type').text.strip()
        desc3 = moto.find('p', class_='volume').text.strip()
        desc_short = f'{desc1} {desc2} {desc3}'
        data = {
            'name': name, 'desc': desc_short, 'price': price, 'img': img
        }
        result.append(data)
    return result

def prepare_csv():
    with open('motoes.csv', 'w') as file:
        fieldnames = ['Name', 'Price', 'Image URL', 'Description']
        writer = csv.DictWriter(file, fieldnames)
        writer.writerow({
            'Name': 'Name',
            'Price': 'Price',
            'Image URL': 'Image',
            'Description': 'Description',
        })

def write_to_csv(data):
    with open('motoes.csv', 'a') as file:
        fieldnames = ['Name', 'Price', 'Image URL', 'Description']
        writer = csv.DictWriter(file, fieldnames)
        global count
        for moto in data:
            writer.writerow({
                'Name': moto['name'],
                'Price': moto['price'],
                'Image URL': moto['img'],
                'Description': moto['desc'],
            })
            
def main():
    i=1
    c=1
    prepare_csv()
    while True:
        url = 'https://www.mashina.kg/motosearch/all/?page={i}'
        html = response
        soup = get_soup(html)
        data = get_data(soup)
        write_to_csv(data)
        print(f'Спарсили {c} страницу')
        if i == 11:
            break
        i += 1
        c += 1
        
main()


