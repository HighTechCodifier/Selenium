# -*- coding: utf-8 -*-
"""
Description:
    Finding element by name in Selenium:
    Use this when you know the name attribute of an element. With this strategy,
    the first element with a matching name attribute will be returned. If no
    element has a matching name attribute, a NoSuchElementException will be
    raised.
"""

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

# Pass an instance of the Service class to the Chrome class:
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://google.com")

sleep(1)

# Find the id of reject-button for cookies:
search_field = driver.find_element('id', 'W0wltc')

sleep(2)

search_field.click()

sleep(2)

# Find the name of search field:
search_field = driver.find_element('name', 'q')

sleep(1)

# Write the text on the search field:
search_field.send_keys("wikipedia")

sleep(1)

# Enter return-key:
search_field.send_keys(Keys.RETURN)

sleep(3)

# Tear down and quit every thing:
driver.quit()

