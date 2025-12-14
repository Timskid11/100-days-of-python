import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
load_dotenv()

SIMILAR_ACCOUNT = os.getenv("SIMILAR_ACCOUNT")
USERNAME = os.getenv("I_USER")
PASSWORD = os.getenv("I_PASSWORD")
print(SIMILAR_ACCOUNT)
print(USERNAME)
print(PASSWORD)


class InstaFollower :
    def __init__(self):
        self.driver_options=webdriver.ChromeOptions()
        self.driver_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(self.driver_options)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        self.username = self.driver.find_element(By.CSS_SELECTOR,"input[aria-label='Phone number, username, or email']")
        self.username.send_keys(USERNAME)
        self.pwd = self.driver.find_element(By.CSS_SELECTOR, "input[aria-label='Password']")
        self.pwd.send_keys(PASSWORD + Keys.ENTER)

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")

        time.sleep(8.2)
        # The xpath of the modal will change over time. Update yours accordingly.
        modal_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]"
        modal = self.driver.find_element(by=By.XPATH, value=modal_xpath)
        for folowwers_page_of_five in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(3)
    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "._aano button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()
insta = InstaFollower()
insta.login()
insta.find_followers()
insta.follow()




