import requests
from bs4 import BeautifulSoup
from threading import Timer
import os
from twilio.rest import Client
import smtplib
import urllib.request



URL = input("Enter URL of the product: ")
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36', 
'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language' : 'en-US,en;q=0.5',
'Accept-Encoding' : 'gzip',
'DNT' : '1', # Do Not Track Request Header
'Connection' : 'close'
} 

set_price = int(input("\nEnter the wish price you want to buy :  "))

def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    rec_email=input("\nEnter Your Email id :  ")

    title = soup.find(id='productTitle').get_text()
    product_title = str(title)
    product_title = product_title.strip()
    print(product_title)
    price = soup.find("span", {"class": "a-price-whole"}).get_text()
    product_price = ''
    for letters in price:
        if letters.isnumeric() or letters == '.':
            product_price += letters
    print(float(product_price))
    
    if float(product_price) <= set_price:
        sender_email="deflationnotify@gmail.com"
        password="tjfvhyeqauybnsfh"
        server= smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(sender_email,password)
        subject = 'Price Drop Alert!!!'
        body = "Your product {}  is available at {}\n\nProduct Link : {}".format(product_title,float(product_price),URL)
        message = f"Subject : {subject}\n\n{body}"
        server.sendmail(sender_email,rec_email,message)
        print("\n")
        print('Email sent')
        print("\n")
        account_sid = "AC91774c84ffddfa35c05adf5c0861fd68"
        auth_token = "4ea1c49612d179555d1534302db4d190"
        account_sid = "AC91774c84ffddfa35c05adf5c0861fd68"
        auth_token = "4ea1c49612d179555d1534302db4d190"
        
        client = Client(account_sid, auth_token)
        client.messages.create(
    to="+919972281280",
    from_="+18176703886",
    body = "Your product {}  is available at {}\n\nProduct Link : {}".format(product_title,float(product_price),URL))
        message = f"Subject : {subject}\n\n{body}"
        print(' Message sent')
        return
    else:
        print('not sent')
    Timer(60, check_price).start()
    
    
check_price()
    