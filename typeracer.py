from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Firefox()
driver.get("https://play.typeracer.com/")

time.sleep(2)

# sends keys?
elem = driver.find_element_by_tag_name('body')
elem.send_keys(Keys.ALT + Keys.CONTROL + 'O')

typeText = input("Enter text")
print(typeText)
