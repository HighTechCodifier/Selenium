# -*- coding: utf-8 -*-
"""
 Description:
    From Selenium version 4.0  executable_path has been deprecated.
    To resolve the issue one should use an instance of the Service
    class and pass in a "Service object" instead.
"""

from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

# Pass an instance of the Service class to the Chrome class:
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Navigate (open) to a page given by the URL:
driver.get('https://www.yahoo.com')

sleep(3)

driver.quit()
