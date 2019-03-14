from bs4 import BeautifulSoup
import requests
import csv

x=input("Enter the ASIN id of the product\n")

source=requests.get("https://www.amazon.in/dp/B07B4QWRSJ").text

soup=BeautifulSoup(source,"lxml")

# B07B4QWRSJ

Name=soup.find('div',id='quickPromoBucketContent')
value=Name

print(value)




