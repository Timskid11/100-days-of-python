from selenium import webdriver
from selenium.webdriver.common.by import By
driver_options = webdriver.ChromeOptions()
driver_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=driver_options)
driver.get("https://www.python.org")
titles = []
times = []
event_times= driver.find_elements(By.CSS_SELECTOR,".event-widget time ")
for time in event_times:
    times.append(time.text)

event_title = driver.find_elements(By.CSS_SELECTOR,".event-widget li a")
for title in event_title:
    titles.append(title.text)

full_dict = {detail:{'time':times[detail],'name': titles[detail]} for detail in range(len(event_title)-1)}
print(full_dict)
driver.quit()