import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time

def sendMail(subject,body):
    msg = MIMEText(body)
    msg['subject'] = subject
    msg['From'] = 'sayhimage@outlook.com'
    msg['To'] = 'sayhimage@outlook.com'
    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()

bsObj = BeautifulSoup(urlopen('https://isitchristmas.com'))
while(bsObj.find('a',{'id':'answer'}).attrs['title'] == 'NO'):
    print('It is not Christmas yet.')
    time.sleep(8888)
    bsObj =BeautifulSoup(urlopen('https://isitchristmas.com.'))
sendMail('It\'s Christmas!','According to http://itischristmas.com,\
    it Christmas')
