import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint

file = open('result.csv', 'w', encoding='utf-8_sig', newline='\n')
file_obj = csv.writer(file)
file_obj.writerow(['სათაური', 'ავტორი', 'ფასი'])
for ind in range(1, 4):
    url = f'https://www.sulakauri.ge/wignebi/?swoof=1&age=8-12&top_category=sabavshvo-literatura-inglisurad&product-page={str(ind)}'
    r = requests.get(url)

    soup = BeautifulSoup(r.text, "html.parser")

    main_holder = soup.find('div', class_='mkdf-pl-main-holder')
    books = main_holder.find('ul', class_='products')

    for book in books.find_all('li', class_='product'):
        title = book.find('h5', class_='mkdf-product-list-title').text.strip()
        author = book.find('div', class_='mkdf-pl-author-holder').text.strip()
        price = book.find('span', class_='price').text.strip()

        print(title, author, price)

        file_obj.writerow([title, author, price])

    sleep(randint(1, 5))

file.close()
