from selenium import webdriver
from selenium.webdriver.common.by import By

driver_options = webdriver.ChromeOptions()
driver_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=driver_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

digit = driver.find_elements(By.CSS_SELECTOR, "#articlecount a")
anchor = digit[1]
anchor.click()


driver.quit()