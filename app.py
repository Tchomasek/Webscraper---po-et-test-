# import libraries
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from datetime import date
import smtplib
from email.mime.text import MIMEText



while True:

    # specify the url
    urlpage = 'https://onemocneni-aktualne.mzcr.cz/covid-19#sekce-1'
    # run firefox webdriver from executable path of your choice
    driver = webdriver.PhantomJS(executable_path = r'C:\Users\x\Desktop\Python\Webscraper\phantomjs-2.1.1-windows\bin\phantomjs')
    # get web page
    driver.get(urlpage)
    time.sleep(2)
    all= driver.page_source
    soup=BeautifulSoup(all, "html.parser")
    testy = soup.find("div",{"id":"js-total-tests-fortnight-data"})
    tab = soup.find("table",{"id":"js-total-tests-table"})
    tr = tab.find_all("tr", {"role":'row'})

    result = []
    for i in tr:
        td = i.find_all("td")
        for j in td:
            result.append(j.text)
    count = result[1]

    datum = str(result[0])
    datum = datum.split('.')
    datum = str(datum[2]+'-'+datum[1]+'-'+str(int(datum[0])+1))
    if datum == str(date.today()):
        print('včerejší počet testů', count, 'odeslán na mail')
        from_email="tompython8@gmail.com"
        from_password="Python11"
        to_email='tchom.asek@centrum.cz'
        subject="Včerejší počet testů"
        message=count
        msg=MIMEText(message, 'html')
        msg['Subject']=subject
        msg['To']=to_email
        msg['From']=from_email
        gmail=smtplib.SMTP('smtp.gmail.com',587)
        gmail.ehlo()
        gmail.starttls()
        gmail.login(from_email, from_password)
        gmail.send_message(msg)
    else:
        print('not updated')
    time.sleep(300)
