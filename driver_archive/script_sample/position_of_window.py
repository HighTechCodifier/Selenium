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

# Get the position of the window:
window_position = driver.get_window_position()

print()
print(window_position)
x_pos = window_position['x']
y_pos = window_position['y']
print(f"x_pos  =  {x_pos} \ny_pos =  {y_pos}")

print("-------------------------------")

sleep(2)

# set a new position for the window:
driver.set_window_position(300, 300)

new_window_position = driver.get_window_position()

# Expected value for x_pos:
expected_x_pos = 300
expected_y_pos = 300

# Assertions:
assert expected_x_pos
assert expected_y_pos

sleep(2)

# Print new positions if the assertion passes:
print(new_window_position)
new_x_pos = new_window_position['x']
new_y_pos = new_window_position['y']
print(f"new_width  =  {new_x_pos} \nnew_height =  {new_y_pos}")

driver.quit()


