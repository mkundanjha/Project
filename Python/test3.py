import nltk
from nltk.corpus import stopwords
s= set(stopwords.words('english'))
#print(s)
l=['what','is','machine','learning']
for i in range(len(l)):
    if (l[i] in s)==False:
        print(l[i])





