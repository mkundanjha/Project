#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import json


# For ignoring SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Taking input from user


while True:
    k=int(input("Search Product using\n 1. url   2.ASIN id \n"))
    if k==1:
        url=input("Enter the url: ")
        break
    elif k==2:
        ASIN=input("Enter the ASIN id: ")
        url='https://www.amazon.in/dp/'+ASIN
        break
    else:
        print("Worng Input--- Enter again\n")


print("\nPlease wait loading.....")


html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
html = soup.prettify('utf-8')

# This block of code will help extract the Prodcut Title of the item
for spans in soup.findAll('span', attrs={'id': 'productTitle'}):
    name_of_product = spans.text.strip()
    print("\nName: ")
    print(name_of_product)
    break

# This block of code will help extract the price of the item in dollars
for divs in soup.findAll('div'):
    try:
        price = str(divs['data-asin-price'])
        print("\nPrice: ")
        print(price)
        break
    except:
        pass


# This block of code will help extract the average star rating of the product
for i_tags in soup.findAll('i',
                           attrs={'data-hook': 'average-star-rating'}):
    for spans in i_tags.findAll('span', attrs={'class': 'a-icon-alt'}):
        print("\nRatings: ")
        print(spans.text.strip())
        break

# This block of code will help extract top specifications and details of the product
#product_json['details'] = []
details=[]
for ul_tags in soup.findAll('ul',attrs={'class': 'a-unordered-list a-vertical a-spacing-none'}):
    for li_tags in ul_tags.findAll('li'):
        for spans in li_tags.findAll('span',
                attrs={'class': 'a-list-item'}, text=True,
                recursive=False):
            details.append(spans.text.strip())
            
print("\nDetails of the Product:\n")
for i in details:
    print(i,end=" ")

print()


