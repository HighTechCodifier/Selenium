# -*- coding: utf-8 -*-
"""
Finding element by absolute_XPATH
    Description:
        What is XPath in Selenium?
        XPath in Selenium is an XML path used for navigation through the HTML
        structure of the page. It is a syntax or language for finding any
        element on a web page using XML path expression. XPath can be used for
        both HTML and XML documents to find the location of any element on a
        webpage using HTML DOM structure.

        In Selenium automation, if the elements are not found by the general
        locators like id, class, name, etc. then XPath is used to find an
        element on the web page.

        Absolute XPath:
        It is the direct way to find the element, but the disadvantage of the
        absolute XPath is that if there are any changes made in the path of the
        element then that XPath gets failed.

        The key characteristic of XPath is that it begins with the single
        forward slash(/) ,which means you can select the element from the root
        node.

        Below is a basic example of locating element by implementing
        absolute-XPath expression:
"""

from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

# Pass an instance of the Service class to the Chrome class:
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://wikipedia.com")

# Find element by absolute_XPATH:
expression = '/html/body/div[3]/form/fieldset/div/input'
element = driver.find_element('xpath', expression)

print()
print(element)

element.send_keys("Hello world!")

sleep(3)

driver.quit()
