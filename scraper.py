import requests 
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.com/BenQ-EX3501R-Gaming-Monitor-FreeSync/dp/B077P62F8X/ref=sr_1_3?keywords=benq+ex3501r&qid=1562621606&s=gateway&sr=8-3'
 
# google search 'my user agent'
headers = {
    "Billy Bob": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
} # noneType error -- swith "User-Agent" to random key

# make a call
def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = int(price[1:4])

    if(converted_price > 525):
        send_mail()

    print(title.strip())
    print(f"${converted_price}")


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('dansvans.peters@gmail.com', 'gtczbvastzlzttsz')
    # secure credentials because 2FA is enabled for google (two step verification required from untrusted devices)
    subject = "Price fell down!"
    body = "Check the amazon link https://www.amazon.com/BenQ-EX3501R-Gaming-Monitor-FreeSync/dp/B077P62F8X/ref=sr_1_3?keywords=benq+ex3501r&qid=1562621606&s=gateway&sr=8-3"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
          'dansvans.peters@gmail.com',
          'dansvans.peters@gmail.com',
          msg
    )
    print("HEY EMAIL HAS BEEN SENT!")

    server.quit()

while True:
    check_price()
    time.sleep(60*60*24)
# page = requests.get(URL, headers=headers)

# soup = BeautifulSoup(page.content, 'html.parser')

# title = soup.find(id="productTitle").get_text()

# print(title.strip())
# print(soup.prettify())