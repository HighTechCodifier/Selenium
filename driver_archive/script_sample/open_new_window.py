# -*- coding: utf-8 -*-
"""
Description:
    Opening a new window
"""

from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

# Pass an instance of the Service class to the Chrome class:
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Navigate (open) to a page given by the URL:
driver.get('https://www.lunduniversity.lu.se/')

sleep(1)

# Open a new window and switch to it:
driver.switch_to.new_window('window')

# Navigate to a page given by the URL:
driver.get('https://www.kth.se/')

sleep(2)

