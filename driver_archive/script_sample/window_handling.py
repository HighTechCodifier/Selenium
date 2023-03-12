# -*- coding: utf-8 -*-
"""
Description:
    Window-handling
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

"""
Get the handle of the current window and stor 
its ID in a variable. It deals with the window
in focus at the moment. It returns the window 
handle id as a string value.
"""
kth_window_handler_id = driver.current_window_handle
print(f"\nkth_window_handler-id  =  {kth_window_handler_id}")

"""
Get all the handle ids of the windows that
are currently open. The collection of window 
handle ids is returned as a set data structure.
"""
all_window_handler_ids = driver.window_handles
print(f"\nall_window_handlers_ids  =  {all_window_handler_ids}")

number_of_all_window_handlers = len(all_window_handler_ids)
print(f"Number of all window-handlers  =  {number_of_all_window_handlers }")

sleep(1)

# Switch to another window with index 0:
driver.switch_to.window(all_window_handler_ids[0])

sleep(3)
