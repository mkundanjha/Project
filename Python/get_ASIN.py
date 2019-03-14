s="https://www.amazon.in/Adidas-Mysblu-Running-Shoes-8-CI9827/dp/B07B4QWRSJ/ref=lp_16374498031_1_1?s=apparel&ie=UTF8&qid=1552497413&sr=1-1"
s=s.split("/")
#print(s)
print()
for x in s:
    if x=="dp":
        k=s.index(x)+1
     

print("The ASIN id for the product is ",s[k])
