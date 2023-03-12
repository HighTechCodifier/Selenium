# -*- coding: utf-8 -*-
"""
Description:
    Maximize or minimize a window.
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

# Get the position of the window:
window_position = driver.get_window_position()
print()
print(window_position)

sleep(2)

# set a new position for the window:
driver.set_window_position(300, 300)

sleep(2)

# Minimize window position:
driver.minimize_window()

sleep(2)

# Maximize window position
driver.maximize_window()

sleep(2)

driver.quit()


