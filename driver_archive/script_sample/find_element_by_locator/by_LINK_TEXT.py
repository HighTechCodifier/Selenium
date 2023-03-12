# -*- coding: utf-8 -*-
"""
Finding element by a certain link-text:
    Description:
        Use this when you know the link-text used within an anchor tag. With
        this strategy, the first element with the link text matching the
        provided value will be returned. If no element has a matching link-text
        attribute, a NoSuchElementException will be raised.

        Below is a basic example of locating element by implementing a certain
        link-text:
"""

from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

# Pass an instance of the Service class to the Chrome class:
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://wikipedia.com")

# Find element by implementing a certain link-text:
value = 'Google Play Store'
element = driver.find_element('link text', value)

sleep(3)

element.click()

sleep(3)

driver.quit()
