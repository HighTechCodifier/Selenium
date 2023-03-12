# -*- coding: utf-8 -*-
"""
Description:
    Opening a new tab
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

sleep(1)

driver.switch_to.new_window('tab')

sleep(2)
