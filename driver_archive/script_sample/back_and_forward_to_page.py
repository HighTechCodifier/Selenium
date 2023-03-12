
# -*- coding: utf-8 -*-
"""
How to back to previous webpage
"""

from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

# Pass an instance of the Service class to the Chrome class:
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


'''
Browser action 1: 
navigate (open) to a page given by the URL:
'''
driver.get("https://google.com")

'''
Read title property of the
web driver object to variable
window_title
'''
window_title = driver.title
# print the page title in console
print(window_title)

sleep(1)

driver.get('https://www.lunduniversity.lu.se/')

window_title = driver.title
print(window_title)

sleep(1)

driver.back()

window_title = driver.title
print(window_title)

sleep(1)

driver.forward()

window_title = driver.title
print(window_title)

sleep(1)

