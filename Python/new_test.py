import requests
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
import csv

source=requests.get('http://tatainnoverse.com/').text

soup=BeautifulSoup(source,'lxml')

s= set(stopwords.words('english'))

csv_file=open('challenge_data_copy.csv','w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['Problem Name','Content'])

contentList=[]
badList=[".",",","'",";",":"]

challenge=soup.find('div',class_='content')

header=challenge.h3.text
content=challenge.p.text
token_content=nltk.word_tokenize(content)
for i in range(len(token_content)):
    if (token_content[i] in s)==False and (token_content[i]!="We") and (token_content[i]!="looking") :
        contentList.append(token_content[i])
    
for element in contentList:
    if (element in badList):
        contentList.remove(element)
 

              
csv_writer.writerow([header,contentList])
contentList=[]
    
  
    


csv_file.close()
