from selenium import webdriver
import time

tarayici = webdriver.Firefox()
tarayici.get("https://www.instagram.com")

#deneme


time.sleep(2)
tarayici.find_element_by_xpath('//input[@name=\"username\"]')\
        .send_keys("Please Input your Username")                                                             
                                            
tarayici.find_element_by_xpath('//input[@name=\"password\"]')\
        .send_keys("Please input your password")                                                            

tarayici.find_element_by_xpath('//button[@type="submit"]')\
         .click()
time.sleep(3)
tarayici.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')\
        .click()
time.sleep(2)
tarayici.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')\
        .click()
time.sleep(1)


for i in range(5):
    
    
    for i in range(5):
        tarayici.find_element_by_xpath('//button[text()="Takip Et"]')\
                .click()
        time.sleep(1)
    tarayici.refresh()
