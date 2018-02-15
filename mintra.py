import requests
from bs4 import BeautifulSoup
url = "https://www.myntra.com/womens-western-wear"
headers = {'User-Agent':'Mozilla/5.0'}
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
all_divs=soup.find_all("div")
print(all_divs)
