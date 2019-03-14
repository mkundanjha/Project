from bs4 import BeautifulSoup
import requests
import csv

url=requests.get('https://www.amazon.in/dp/B075SCBTGW').text

soup=BeautifulSoup(url,'html.parser')


csv_file=open('index.csv','w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['Name'])

for spans in soup.findAll('span', attrs={'id': 'productTitle'}):
    name_of_product = spans.text.strip()
    csv_writer.writerrow([name_of_product])
    break

csv_file.close()



