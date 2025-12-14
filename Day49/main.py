from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import time
from dotenv import load_dotenv
from selenium.common.exceptions import NoSuchElementException


role = input("What role you do you want to apply for? ")

load_dotenv()

linkedin_options = webdriver.ChromeOptions()
linkedin_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=linkedin_options)
driver.get("https://www.linkedin.com/checkpoint/rm/sign-in-another-account?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")

mail = os.getenv("MAIL")
password = os.getenv("PASSWORD")


m_input = driver.find_element(By.ID, "username")
p_input = driver.find_element(By.ID, "password")
button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[4]/button')

m_input.send_keys(mail)
p_input.send_keys(password)
button.send_keys(Keys.ENTER)

time.sleep(5)
job_button = (driver.find_elements(By.CSS_SELECTOR, ".global-nav__primary-items a"))[2]
job_button.click()
time.sleep(5)
search_button = driver.find_element(By.XPATH,'//*[@id=":r5:"]')
search_button.click()
search_button.send_keys(role)
search_button.send_keys(Keys.ENTER)
time.sleep(5)
jobs = driver.find_elements(By.CSS_SELECTOR,'.daSgvLxsFvfhoQSwTgAOQriEXhCrcmPPA li a')
time.sleep(5)
for job in jobs:
    job.click()
    time.sleep(5)
    try:
        apply = driver.find_element(By.ID,'jobs-apply-button-id')
        apply.click()
        submit_button = driver.find_element(By.CSS_SELECTOR,'#ember1129 .artdeco-button__text')
        button.click()
    except NoSuchElementException:
        print(f'Application requires manual context\nHere is the link:\n{job.get_attribute('href')}')
