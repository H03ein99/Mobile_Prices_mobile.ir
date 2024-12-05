import requests
from bs4 import BeautifulSoup
import re
# print the price of a brand you want in 10 pages of mobile.ir
brands =['Samsung', 'Apple', 'Huawei', 'Xiaomi']
num = int(input("for samsung enter 1 for apple enter 2 for huawei enter 3 and for xiaomi enter 4: ")) - 1
counter = 0
for i in range(10):
    if i == 0:
        r = requests.get('https://www.mobile.ir/phones/prices.aspx')
    else:
        r = requests.get('https://www.mobile.ir/phones/prices.aspx?page=%i' % (i + 1))
    soup = BeautifulSoup(r.text, 'html.parser')
    all_prices = soup.find('table', attrs={"id": "price_table"})
    phones = all_prices.find_all('tr')
    checker = brands[num]
    for phone in phones:
        link = phone.find('a', attrs={'class': "phone"})
        name = re.findall(r"\"\>(.*)\<", str(link))
        price_link = phone.find('td', attrs={"class": "price"})
        price = re.findall(r"aspx\"\>(.*)\<\/a", str(price_link))
        try:
            name = name[0]
            price = price[0]
            if checker in name:
                counter += 1
                print(f"{counter}- {name}: {price}")
        except:
            continue



