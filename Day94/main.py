from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from PIL import ImageGrab

bot = webdriver.ChromeOptions()
bot.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=bot)
driver.get("https://elgoog.im/t-rex/")

time.sleep(3)  # wait for game to load

body = driver.find_element(By.TAG_NAME, "body")
DETECTION_BOX = (450, 500, 520, 560)
BACKGROUND_THRESHOLD = 230
JUMP_COOLDOWN = 0.25

# Start jumping forever
while True:
    image = ImageGrab.grab(bbox=DETECTION_BOX)
    pixels = image.getdata()
    for r, g, b in pixels:
        brightness = (r + g + b) / 3
        if brightness < BACKGROUND_THRESHOLD:
            body.send_keys(Keys.SPACE)
            time.sleep(JUMP_COOLDOWN)
            break




