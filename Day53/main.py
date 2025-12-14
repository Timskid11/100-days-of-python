import selenium
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests
import time
response = requests.get('https://appbrewery.github.io/Zillow-Clone/')
response.raise_for_status()
response = response.text
soup = BeautifulSoup(response, 'html.parser')

rent_list_address = soup.select(".ListItem-c11n-8-84-3-StyledListCardWrapper address")
rent_link_price = soup.select(".ListItem-c11n-8-84-3-StyledListCardWrapper .PropertyCardWrapper__StyledPriceLine")
rent_list_link =soup.select(".ListItem-c11n-8-84-3-StyledListCardWrapper a")
#USe this for addr and price
#.text.strip()
#USe this for link
#['href']
#My selenium part

driver_options = webdriver.ChromeOptions()
driver_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=driver_options)
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdn6XIu4GZWVkejGZKDJ545S3l6VYeDY05-rkAHKZd6mIRDMA/viewform")

time.sleep(2)
for each_rent in range(len(rent_list_link)):
    addr_input = driver.find_element(By.XPATH,
                                     '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input = driver.find_element(By.XPATH,
                                      '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input = driver.find_element(By.XPATH,
                                     '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit = driver.find_element(By.CSS_SELECTOR, 'div[role = "button"]')

    addr_input.click()
    addr_input.send_keys(rent_list_address[each_rent].text.strip())
    price_input.click()
    price_input.send_keys(rent_link_price[each_rent].text.strip())
    link_input.click()
    link_input.send_keys(rent_list_link[each_rent]["href"].strip())
    submit.click()
    time.sleep(1)
    another_response = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_response.click()
    time.sleep(1)

driver.quit()
print(f"{len(rent_list_link)} rent infos have been added")



