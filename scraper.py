import requests
from bs4 import BeautifulSoup

import smtplib

import time

URL = 'https://www.amazon.com/s?k=computer+desk+home+office+workstation&gclid=EAIaIQobChMI5rCrwobi4wIVA6rsCh3dWgX8EAAYASAAEgJbRPD_BwE&hvadid=366132129575&hvdev=c&hvlocphy=9031026&hvnetw=g&hvpos=1t1&hvqmt=b&hvrand=5977377612335491817&hvtargid=kwd-791397541860&hydadcr=18745_9862727&tag=googhydr-20&ref=pd_sl_59p1hb4joy_b'

headers = {"User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'} 

def check_price():

    page = requests.get(UrL, headers=headers)

    soup = BeautifulSoup(page.contect, 'html.parser')

    title = soup.find(id="productTitle").get_text()

    price = soup.find(id="priceblock_ourprice").get_text()

    convert_price = float(price[0:5]) 

    if(convert_price < 1.700): 
        send_mail()

    print(convert_price)
    print(title.strip())

    if(convert_price < 1.700)
        send_mail()


def sent_mail():

    server = smtplib.SMIP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('cnhahn@ucsc.edu', 'zsphinqrkqmvjahj')

    subject = 'Price fell down!'
    body = 'Check the amazon link https://www.amazon.com/s?k=computer+desk+home+office+workstation&gclid=EAIaIQobChMI5rCrwobi4wIVA6rsCh3dWgX8EAAYASAAEgJbRPD_BwE&hvadid=366132129575&hvdev=c&hvlocphy=9031026&hvnetw=g&hvpos=1t1&hvqmt=b&hvrand=5977377612335491817&hvtargid=kwd-791397541860&hydadcr=18745_9862727&tag=googhydr-20&ref=pd_sl_59p1hb4joy_b'

    msg = f"Subject : {subject}\n\n{body}"

    server.sendmail(
        'cnhahn@ucsc.edu',
        'chrissy.n.hahn@gmail.com',
        msg
    )

    print('message was sent via email')

    server.quit()
    
while(True):

    check_price()
    time.sleep(60 * 60)