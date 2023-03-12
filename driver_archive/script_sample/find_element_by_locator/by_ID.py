# -*- coding: utf-8 -*-
"""
Description:
    Finding element by ID in Selenium:
    Use this when you know the id attribute of an element. With this strategy,
    the first element with a matching id attribute will be returned. If no
    element has a matching id attribute, a NoSuchElementException will be
    raised.
"""

from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

# Pass an instance of the Service class to the Chrome class:
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://wikipedia.com")

# Find element by ID:
element = driver.find_element('id', 'searchInput')

element.send_keys("Hello world!")

sleep(3)

driver.quit()
