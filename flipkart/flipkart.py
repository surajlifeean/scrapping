import requests
from bs4 import BeautifulSoup
url = "https://www.flipkart.com/womens-clothing/western-wear/pr?sid=2oq,c1r,ha6&otracker=categorytree&otracker=nmenu_sub_Women_0_Western%20Wear"
headers = {'User-Agent':'Mozilla/5.0'}
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
all_divs=soup.find("div",class_='GQtpzo')
i=0
for div in all_divs:
    #name=a.find("a",class_='_2cLu-l')
    if(i==2):
        j=0;
        for pro in div.findAll("div",class_='_3liAhj'):
            #print(pro)
            product=pro.find("a",class_='_2cLu-l')
            price=pro.find("div",class_='_1vC4OE')
            print(product.text)
            print(price.text)
            print('-------------------------------------------------------------------------------------------------------------------------------',j)
            j=j+1
    i=i+1
