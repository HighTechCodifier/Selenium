# -*- coding: utf-8 -*-
"""
Description:
    Taking a screenshot
"""


import os.path    # Provides functions for interacting with the operating system.
from pathlib import Path
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

"""
Using the path-module to get the parent
of current directory. 
Also use ".parent" to fetch the parent of
the current directory.
"""
current_path = Path(__file__).parent
# Convert it to a string:
current_path_as_string = str(current_path)

"""
use os.path.join() method to join one or more path 
components intelligently. This method concatenates
various path components with exactly one directory 
separator (‘/’) following each non-empty part except
the last path component. If the last path component
to be joined is empty then a directory separator (‘/’) 
is put at the end. If a path component represents an
absolute path, then all previous components joined are
discarded and joining continues from the absolute path
component. NOTE: it must be a png-file
"""
file_name = os.path.join(current_path_as_string, "Screenshot_1.png")

"""
Save a screenshot of the 
page at current status
and save it in the
file_name:  
"""
driver.save_screenshot(file_name)

sleep(1)

driver.quit()
