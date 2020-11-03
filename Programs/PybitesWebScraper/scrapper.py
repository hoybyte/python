import requests
import bs4
import pprint
import re

site = requests.get("https://codechalleng.es/bites/catalogue")
site_data = site.text

soup = bs4.BeautifulSoup(site_data, 'html.parser')
html_header_list = soup.select('.link')

header_list = []

for headers in html_header_list:
    header_list.append(headers.getText())

info = []

for headers in header_list:
    item = re.sub(r'[\n            \n            ]', '',  headers)
    info.append(item)

pprint.pprint(info)
print(info)
