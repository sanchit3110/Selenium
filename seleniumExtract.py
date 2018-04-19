from selenium import webdriver
import os, time
from selenium.webdriver.common.keys import Keys

#csv file
import csv

#from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
chromedriver = "C:\Users\Admin\Downloads\chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
#outputFile = open("imagesList90000_91100.txt","w")
driver = webdriver.Chrome(chromedriver)
count = 0


#getting events from txt begin
fileEventList = open("list.txt","r")
v = fileEventList.readlines()
EventList = []

for x in v:
    EventList.append(int(x.strip()))

#print EventList

#getting events from txt end


#EventList = [91119, 90018, 90005]
#for i in range(90000,91100,1):

with open('seleniumExtract35_2.csv', 'wb') as csvfile:
    filewriter = csv.writer(csvfile)
    filewriter.writerow(['EventId','Date_of_Sighting', 'Date_of_Report','Description','Duration','Shape','City','Region','Country','Longitude','Latitude','Photos'])
    #filewriter.writerow([sightingDate,reportDate,description,duration,shape,city,region,country,longitude,latitude,photoList])
    for event in EventList:
        #static for file 91156
        driver.get("http://www.ufostalker.com/event/"+str(event))


        sightingDate = ""
        reportDate = ""
        description = ""
        duration = ""
        shape = ""
        city = ""
        region = ""
        country = ""
        longitude = ""
        latitude = ""

        
        
    
        

        #Date of sighting
        date_of_sighting = driver.find_elements_by_xpath("//tr[@ng-hide='!event.occurred']//b[@class='ng-binding']")
        if len(date_of_sighting)>0:
            sightingDate = date_of_sighting[0].get_attribute('innerHTML')
            #print sightingDate

        #Date of report
        date_of_report = driver.find_elements_by_xpath("//tr[@ng-hide='!event.submitted']//b[@class='ng-binding']")
        if len(date_of_report)>0:
            reportDate = date_of_report[0].get_attribute('innerHTML')
            #print reportDate

        #Description
        #desc = driver.find_element_by_id("summary")
        #description = desc.get_attribute('innerHTML')
        #temporary set to null
        description = ""
        #print description


        #duration
        dur = driver.find_elements_by_xpath("//tr[@ng-hide='!event.duration']//td[@class='ng-binding']")
        if len(dur)>0:
            duration = dur[0].get_attribute('innerHTML')
            #print duration

        #shape
        sha = driver.find_elements_by_xpath("//tr[@ng-hide='!event.shape']//td[@class='ng-binding']")
        if len(sha)>0:
            shape = sha[0].get_attribute('innerHTML')
            #print shape

        #city
        cit = driver.find_elements_by_xpath("""//tr[@ng-hide="!event.city || event.city == '?'"]//td//a//b[@class='ng-binding']""")
        if len(cit)>0:
            city = cit[0].get_attribute('innerHTML')
            #print city

        #region
        reg = driver.find_elements_by_xpath("""//tr[@ng-hide="!event.region || event.region == '?'"]//td//a//b[@class='ng-binding']""")
        if len(reg)>0:
            region = reg[0].get_attribute('innerHTML')
            #print region


        #country
        coun = driver.find_elements_by_xpath("""//tr[@ng-hide="!event.country || event.country == '?'"]//td[@class='ng-binding']""")
        if len(coun)>0:
            country = coun[0].get_attribute('innerHTML')
            #print country

        #longitude
        lon = driver.find_elements_by_xpath("""//tr[@ng-hide="!event.longitude"]//td[@class='ng-binding']""")
        if len(lon)>0:
            longitude = lon[0].get_attribute('innerHTML')
            #print longitude

        #latitude
        lat = driver.find_elements_by_xpath("""//tr[@ng-hide="!event.latitude"]//td[@class='ng-binding']""")
        if len(lat)>0:
            latitude = lat[0].get_attribute('innerHTML')
            #print latitude


        #photo url
        photoList = []
        photo = driver.find_elements_by_xpath("//td[@ng-repeat = 'url in event.urls']//a")
        photoC = driver.find_elements_by_xpath("//td[@ng-repeat = 'url in event.urls']//a//div")
        #photoCheck = photoC.get_attribute('innerHTML')
        for ival,i in enumerate(photo):
            #photoC = i.find_elements_by_xpath("//div")
            photoCheck = photoC[ival].get_attribute('innerHTML')
            #print photoCheck
            if photoCheck == "Photo":
                photoList.append(i.get_attribute('href'))
            

        #event = event.encode('utf-8').strip()
        #sightingDate = sightingDate.encode('utf-8').strip()
        #reportDate = reportDate.encode('utf-8').strip()
        description = description.encode('utf-8').strip()
        #duration = duration.encode('utf-8').strip()
        shape = shape.encode('utf-8').strip()
        city = city.encode('utf-8').strip()
        region = region.encode('utf-8').strip()
        country = country.encode('utf-8').strip()
        longitude = longitude.encode('utf-8').strip()
        latitude = latitude.encode('utf-8').strip()
        print event

            
        #print photoList
        if len(photoList)>0:
            filewriter.writerow([event,sightingDate,reportDate,description,duration,shape,city,region,country,longitude,latitude,photoList])
        #filewriter.writerow(['Date_of_Sighting', 'Date_of_Report','Description','Duration','Shape','City','Region','Country','Longitude','Latitude','Photos'])



        

