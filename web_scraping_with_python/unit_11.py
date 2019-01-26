from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import subprocess
import request
from PIL import Image
from PIL import ImageOps

def cleanImage(imagePath):
    image = Image.open(imagePath)
    image = image.point(lambda x: 0 if x<143 else 255)
    borderImage = ImageOps.expand(image,border=20,fill='white')
    borderImage.save(imagePath)

html = urlopen('http://www.pythonscraping.com/humans-only')
bsObj = BeautifulSoup(html)

imageLocation = bsObj.find('img',{'title': 'Image CAPTCHA'})['src']
formBuildId = bsObj.find('input',{'name':'form_build_id'})['value']
captchasid = bsObj.find('input',{'name':'captcha_sid'})['value']
captchatoken = bsObj.find('input',{'name':'captcha_token'})['value']

captchaUrl = 'http://pythonscraping.com'+imageLocation
urlretrieve(captchaUrl,'captcha.jpg')
cleanImage('captcha.jpg')
p = subprocess.Popen(['tesseract','captcha.jpg','captcha'],stdout =
    subprocess.PIPE,stderr=subprocess.PIPE)
p.wait()
f = open('captcha.txt','r')

captcharesponse = f.read().replace(' ','').replace('\n','')
print('captcha solution attempt:' + captcharesponse)

if len(captcharesponse) == 5:
    params = {
    'captcha_token':captchaToken,
    'captcha_sid':captchasid,
    'form_id':'comment_node_page_form',
    'form_build_id': formBuildId,
    'captcha_response':captcharesponse,
    'name':'Ryan Mitchell',
    'subject': ' i come to seek the grail'
    'comment_body[und][0][value]':'...and i an definitely not a bot'
    }
r = request.post('http://www.pythonscraping.com/comment/reply/data={}'.format(params)
responseObj = BeautifulSoup(r.text)
if responseObj.fin('div',{'class':'messages'}) is not None:
    print(responseObj.find('div',{'class':'messages'}).get_text())
else:
    print('There was a problem reading the CAPTCHA correctly!')
