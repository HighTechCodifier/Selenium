# -*- coding: utf-8 -*-
"""
Description:
    How to handle size of a window
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

# Get window size and stor it in a variable:
window_size = driver.get_window_size()

print()
print(window_size)
width = window_size['width']
height = window_size['height']
print(f"width  =  {width} \nheight =  {height}")

print("-------------------------------")

sleep(2)
# Set window size and stor it in a variable:
driver.set_window_size(800, 600)

new_window_size = driver.get_window_size()

# Expected value for width:
expected_width = 800
# Expected value for height:
expected_height = 600

# Assertions:
assert expected_width
assert expected_height


# Print size if the assertion passes:
print(new_window_size)
new_width = new_window_size['width']
new_height = new_window_size['height']
print(f"new_width  =  {new_width} \nnew_height =  {new_height}")

sleep(2)

driver.quit()


