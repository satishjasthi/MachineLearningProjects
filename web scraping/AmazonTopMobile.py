import csv
from selenium import webdriver
from bs4 import BeautifulSoup 
from webdriver_manager.chrome import ChromeDriverManager
import requests
import schedule
import time
from csv import writer 

import schedule
import time


# function to get the top 10 mobile list and there discriptions
def Amazon_Top_mobiles():


    # Adding url of amazon on crome driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    url = 'https://www.amazon.in/s?k=top+10+mobiles&ref=nb_sb_noss_1'
    driver.get(url)
    
    #creating soup object of the crome page to extract
    soup = BeautifulSoup(driver.page_source,'lxml')
    result = soup.find_all('div',{'data-component-type':'s-search-result'})

    #function to get Mobile name , specifications , Price , Ratings
    data =[]
    for i  in range(0,10):
        item = result[i]
        atag = item.h2.a
        # extracting Mobile name and Description(RAM and storage)
        mobile =  atag.text.strip()
        ## extracting price
        try:
            price_parent = item.find('span','a-price')
            price =  price_parent.find('span','a-offscreen').text  
        except AttributeError:
            price = None
        #extracting ratings
        try:
            rating =  item.i.text
            Number_of_rating =  item.find('span','a-size-base').text
        except AttributeError:
            rating = None
            Number_of_rating = None
        
        #appending the discrption into data list
        discription = (mobile,price,rating,Number_of_rating)
        data.append(list(discription))

    print(data)
    

    # converting data list into csv file
    for i in range(len(data)):
        # Open our existing CSV file in append mode 
        # Create a file object for this file 
        with open('Amazon_data.csv', 'a') as f_object: 
        
            # Pass this file object to csv.writer() 
            # and get a writer object 
            writer_object = writer(f_object) 
        
            # Pass the list as an argument into 
            # the writerow() 
            writer_object.writerow(data[i]) 
        
            #Close the file object 
            f_object.close() 


#scheduling to run program for every 24 hours
schedule.every(24).hours.do(Amazon_Top_mobiles)

while True:
    schedule.run_pending()
    time.sleep(1)
