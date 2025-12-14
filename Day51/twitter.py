import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By

load_dotenv()
URL='https://www.speedtest.net/'
PROMISED_DOWN = 150
PROMISED_UP = 40
X_MAIL = os.getenv('X_MAIL')
X_PASSWORD = os.getenv('X_PASSWORD')



class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver_options = webdriver.ChromeOptions()
        self.driver_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=self.driver_options)
        self.down = 0
        self.up = 0


    def get_internet_speed(self):
        self.driver.get(URL)
        time.sleep(8)

        go_button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[2]/a')
        go_button.click()

        time.sleep(80)
        self.up = self.driver.find_element(By.XPATH,
                                           value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.down = self.driver.find_element(By.XPATH,
                                             value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text

    def tweet_at_provider(self):
        print(self.up)
        print(self.down)
        self.driver.get("https://x.com/login")
        time.sleep(5)

        #TIme to enter mail
        mail = self.driver.find_element(By.NAME,'text')
        mail.clear()
        mail.send_keys(X_MAIL)
        mail.send_keys(Keys.ENTER)

        next_button = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/button[2]/div')
        next_button.click()


        time.sleep(5)
        password = self.driver.find_element(By.NAME,'password')
        password.send_keys(X_PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(7)

        #time to post
        tweet_body = self.driver.find_element(By.CSS_SELECTOR, 'div[role="textbox"]')
        tweet_body.click()
        time.sleep(1)
        tweet_body.send_keys(f"Hey MTN,why is my internet speed {self.down} down and {self.up} up..When i paid for {PROMISED_DOWN} down/ {PROMISED_UP} up?")
        time.sleep(1)
        post_button = self.driver.find_element(By.CSS_SELECTOR,'button[data-testid="tweetButtonInline"]')
        post_button.click()


ISTB = InternetSpeedTwitterBot()
ISTB.get_internet_speed()
ISTB.tweet_at_provider()





