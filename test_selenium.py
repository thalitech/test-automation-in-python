#!/usr/bin/env python3

# pip3 install selenium

# https://www.seleniumhq.org/download/

# https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz

# sudo apt install python3-pip
# sudo pip3 install selenium
# java -jar selenium-server-standalone-3.141.59.jar
# ./test_selenium.py 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
    desired_capabilities=DesiredCapabilities.FIREFOX)

driver.get("https://www.wikipedia.org/")
assert "Wikipedia" in driver.title
elem = driver.find_element_by_name("search")
elem.clear()
elem.send_keys("brasil")
elem.send_keys(Keys.RETURN)

elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'firstHeading')))
print(elem.text)

driver.close()
