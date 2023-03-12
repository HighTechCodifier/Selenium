# -*- coding: utf-8 -*-
"""
Finding element by a certain class-name:
    Description:
        Use this when you want to locate an element by class-name. With this
        strategy, the first element with the matching class name attribute will
        be returned. If no element has a matching class name attribute, a
        NoSuchElementException will be raised.

        Below is a basic example of locating element by implementing a certain
        class-name:
"""

from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

# Pass an instance of the Service class to the Chrome class:
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://wikipedia.com")

sleep(1)

# Find element by ID:
value = 'searchInput'
element = driver.find_element('id', value)

element.send_keys("Hello world!")

sleep(1)

# Find search-icon element by implementing a class-name:
value = 'svg-search-icon'
element = driver.find_element('class name', value)

element.click()

sleep(3)

driver.quit()

