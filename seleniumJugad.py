from selenium import webdriver
import os, time
from selenium.webdriver.common.keys import Keys

#from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException

#chromedriver path to be changed
chromedriver = "C:\Users\Admin\Downloads\chromedriver"

os.environ["webdriver.chrome.driver"] = chromedriver
outputFile = open("imagesList90347_90500.txt","w")
driver = webdriver.Chrome(chromedriver)
#test code
#options = webdriver.ChromeOptions()
#options.add_argument('--ignore-certificate-errors-spki-list')
#options.add_argument('--ignore-ssl-errors')
#driver = webdriver.Chrome(chrome_options=options)
#test code end
count = 0
for i in range(89305,90000,1):
    driver.get("http://www.ufostalker.com/event/"+str(i))
    titles_element = driver.find_elements_by_xpath("//a[@class='tag ng-binding']")
    tagList = []
    for j in titles_element:
        
        tagList.append(j.get_attribute('innerHTML'))
    
    if 'photo' in tagList:
        count = count + 1
        outputFile.write(str(i))
        outputFile.write("\n")
        print i
outputFile.close()
        

