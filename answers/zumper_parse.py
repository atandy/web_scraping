import requests
import bs4
import csv

url = "https://www.zumper.com/blog/2015/07/the-10-most-luxurious-apartments-for-rent-in-nyc-right-now/"

r = requests.get(url).content

soup = bs4.BeautifulSoup(r)

apts = soup.findAll('h3')

apts_dict_list = []

for apt in apts:
    listing = apt.getText()
    try:
        rank = listing.split('.')[0]
        location = listing.split('.')[1].split(unicode('–','utf-8'))[0]
        info = listing.split(unicode('–','utf-8'))[1].split('$')[0]
        price = listing.split('$')[1]

        d = {
            'rank': rank.encode('utf-8'),
            'location': location.encode('utf-8'),
            'info': info.encode('utf-8'),
            'price': price.encode('utf-8')
        }
        apts_dict_list.append(d)
    except Exception as e:
        pass


with open('luxurious_apts.csv', 'w') as csvfile:
    fieldnames = apts_dict_list[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for apt_dict in apts_dict_list:
        writer.writerow(apt_dict)