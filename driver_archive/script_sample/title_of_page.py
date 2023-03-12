
# -*- coding: utf-8 -*-
"""
Description:
    Title of page
"""

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
Read title the webpage to 
a variable: page_title
'''
page_title = driver.title

# print the page title in console
print(page_title)

'''
Read URL the webpage to 
a variable: page_url
'''
page_url = driver.current_url

# print the current URL in console
print(page_url)



