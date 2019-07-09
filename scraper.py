import requests 
from bs4 import BeautifulSoup

URL = 'https://www.amazon.com/BenQ-EX3501R-Gaming-Monitor-FreeSync/dp/B077P62F8X/ref=sr_1_3?keywords=benq+ex3501r&qid=1562621606&s=gateway&sr=8-3'
 
# google search 'my user agent'
headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}

# make a call
def check_price():
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = int(price[1:4])

    if(converted_price < 525):
        send_mail()

    print(title.strip())
    print(converted_price)

def send_mail():
    


