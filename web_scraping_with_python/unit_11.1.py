import time
from urllib.request import urlretrieve
from selenium import webdriver
import subprocess


driver = webdriver.chrome(executable_path='')
driver.get('http://www.amazon.con/War-Peace-Leo-Nikolayevich-Tolstoy/dp/1427030200')
time.sleep(2)

driver.find_element_by_id('sitbLogoImg').click()
imageList = set()
time.sleep(5)

while 'pointer' in driver.find_element_by_id(
    'sitbReaderRightPageTurner').get_attribute('style'):
    driver.find_element_by_id('sitbReaderRightPageTurner').click()
    time.sleep(2)
    pages = driver.find_element_by_xpath('//div[@class=\'pageImage\']')
    for page in pages:
        image = page.get_attribute('src')
        imageList.add(image)

driver.quit()


for image in sorted(imageList):
    urlretrieve(image,'page.jpg')
    p = subprocess.Popen(['tesseract','page.jpg','page'],
        stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    P.wait()
    f = oprn('page.txt','r')
    print(f.read())
    
