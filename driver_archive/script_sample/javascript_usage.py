# -*- coding: utf-8 -*-
"""
This is an example of executing a Javascript instruction in Selenium webdriver
using Python. Description:
    Some operations like scrolling down in a page cannot be performed by Selenium
    methods directly. This can be done with the help of the Javascript Executor.
    In this example deals with the window.scrollTo method to perform scrolling
    operation in a page.
"""

from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


# Pass an instance of the Service class to the Chrome class:
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# navigate (open) to a page given by the URL:
driver.get('https://www.yahoo.com')

sleep(2)

"""
Execute a Javascript instruction to scroll down in a page. It works like this:
    ¤   A Javascript Executor is applied on the Selenium webdriver.
    ¤   Selenium executes the Javascript commands by taking the help of the 
        execute_script method. 
    ¤   The commands to be executed are passed as arguments to the method. 
    ¤   Here, we use the window.scrollTo method to perform scrolling operation.
    ¤   The pixels to be scrolled horizontally along the x-axis and pixels to be
        scrolled vertically along the y-axis are passed as parameters to the method: 
        -   The Document Object Model communicates with the elements on the page with
            the help of Javascript.
        -   We'll scroll down from the highest point av the page which is "0" to the
            bottom of the page which is "scrollHeight".
"""
driver = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

sleep(10)

# driver.quit()
