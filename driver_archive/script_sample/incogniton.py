# -*- coding: utf-8 -*-
"""
Description:
    Open browser-window in incognito/private mode using python selenium webdriver
"""

from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

# Create an object of the ChromeOptions class
object_of_web_browser = webdriver.ChromeOptions()

# Apply the method add_argument to that object and pass the parameter "--incognito":
object_of_web_browser.add_argument("--incognito")

"""
Pass an instance of the Service class to the Chrome class (with an object of 
chrome options). This is only possible from Selenium #4
"""
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                          options=object_of_web_browser)

'''
Browser action 1: 
navigate (open) to a page given by the URL:
'''
driver.get('https://www.lunduniversity.lu.se/')

sleep(3)

driver.quit()
