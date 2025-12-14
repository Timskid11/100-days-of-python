import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

import time
load_dotenv()
p = os.getenv("p")
e = os.getenv("e")

driver_options = webdriver.ChromeOptions()
driver_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=driver_options)

driver.get("https://tinder.com/")
time.sleep(5)
log_in = driver.find_element(By.XPATH,'//*[@id="s-73203509"]/div/div[1]/div/main/div[1]/div/div/div/div/div[1]/header/div/div[2]/div[2]/a')
log_in.click()

time.sleep(5)
fb_login = driver.find_element(By.XPATH,'//*[@id="s-1801584585"]/div/div/div/div[2]/div/div/div[2]/div[2]/span/div[2]/button')
fb_login.click()


driver.switch_to.window(driver.window_handles[-1])


time.sleep(5)
email = driver.find_element(By.XPATH,'//*[@id="email"]')
password = driver.find_element(By.ID,'pass')
time.sleep(5)
email.click()
email.send_keys(e)
password.click()
password.send_keys(p)
log_in_tinder = driver.find_element(By.NAME,'login')
log_in_tinder.click()

time.sleep(5)
input("Press enter to proceed with automation!")
time.sleep(5)
driver.switch_to.window(driver.window_handles[-1])

dis_like = driver.find_element(By.CLASS_NAME,'gamepad-icon-wrapper')
for x in range(100):
    dis_like.click()

    time.sleep(3)

driver.quit()