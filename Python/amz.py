import requests
from bs4 import BeautifulSoup
#import nltk
#from nltk.corpus import stopwords
import csv

x=input("Enter the ASIN id of the product\n")

source=requests.get("https://www.amazon.in/dp/"+x).text

soup=BeautifulSoup(source,'lxml')

#s= set(stopwords.words('english'))

#csv_file=open('tags_data_copy.csv','w')
#csv_writer=csv.writer(csv_file)
#csv_writer.writerow(['Problem Name','Content'])

tags=soup.find(id='productTitle')
tags_price=soup.find(id='priceblock_ourprice')


Name=tags.text
Price=tags_price.text

print(Name.strip())
print(Price.strip())

#k=''


for details in soup.find_all('div',class_='a-section a-spacing-medium a-spacing-top-small'):
        k=details.span.text
        print(k.strip)



#print(k)
#content=tags.p.text
'''token_content=nltk.word_tokenize(content)
for i in range(len(token_content)):
    if (token_content[i] in s)==False and (token_content[i]!="We") and (token_content[i]!="looking") :
        contentList.append(token_content[i])
    
for element in contentList:
    if (element in badList):
        contentList.remove(element)
 

              
csv_writer.writerow([header,contentList])
contentList=[]
    
  
    


csv_file.close()'''
