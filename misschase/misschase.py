import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://www.flipkart.com/search?q=miss%20chase&otracker=start&as-show=on&as=off"
headers = {'User-Agent':'Mozilla/5.0'}
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
all_divs=soup.find("div",class_='GQtpzo')
i=0
A=[]
B=[]
for div in all_divs:
    #name=a.find("a",class_='_2cLu-l')
    if(i==2):
        j=0;
        for pro in div.findAll("div",class_='_3liAhj'):
            #print(pro)
            product=pro.find("a",class_='_2cLu-l')
            price=pro.find("div",class_='_1vC4OE')
            #print(product.text)
            #print(price.text)
            A.append(product.text)
            B.append(price.text)
            j=j+1
    i=i+1
df=pd.DataFrame(A,columns=['Product'])
df['Price']=B
print(df)
