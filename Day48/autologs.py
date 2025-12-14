from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver_options = webdriver.ChromeOptions()
driver_options.add_experimental_option("detach", True)

driver = webdriver.Chrome()
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
last_name = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")
button = driver.find_element(By.CSS_SELECTOR,'button')

first_name.send_keys("Timilehin")
last_name.send_keys("Oyinlola")
email.send_keys("timiTheEngineer@gmail.com")
button.send_keys(Keys.ENTER)

