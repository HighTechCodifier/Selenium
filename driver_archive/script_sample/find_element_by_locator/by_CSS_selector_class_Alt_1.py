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
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

# Pass an instance of the Service class to the Chrome class:
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://wikipedia.com")

sleep(1)

"""
Find element by implementing a class-name:
As it is we are using an ID as our CSS selector we need to
put a # in front of the id-name
"""
element = driver.find_element(By.CSS_SELECTOR, '#searchInput')

element.send_keys("Hello world!")

sleep(1)

"""
Find search-icon element by implementing a class-name:
As it is we are using a class as our CSS selector we 
need to use a dot-notation (i.) in front of the class-name.
"""
element = driver.find_element(By.CSS_SELECTOR, 'i.svg-search-icon')

element.click()

sleep(3)

driver.quit()

