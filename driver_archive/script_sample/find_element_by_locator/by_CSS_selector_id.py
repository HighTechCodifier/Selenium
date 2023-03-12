# -*- coding: utf-8 -*-
"""
Finding element by a certain class-name:
    Description:
        Use this when you want to locate an element using CSS selector syntax.
        With this strategy, the first element matching the given CSS selector
        will be returned. If no element matches the provided CSS selector, a
        NoSuchElementException will be raised.

        Below is a basic example of locating element by implementing a CSS
        selector:
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
value = '#searchInput'
element = driver.find_element('css selector', value)

element.send_keys("Hello world!")

sleep(1)

# Find element by implementing a class-name:
value = '.svg-search-icon'       # NOTE the point in front of the class name
element = driver.find_element('css selector', value)

element.click()

sleep(3)

driver.quit()

