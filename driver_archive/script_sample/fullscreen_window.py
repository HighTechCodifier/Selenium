# -*- coding: utf-8 -*-
"""
Description:
    How to get a full-screen Chrome window
    in Selenium Webdriver using python
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
driver.get('https://www.lunduniversity.lu.se/')

sleep(2)

driver.fullscreen_window()

sleep(3)

driver.quit()
