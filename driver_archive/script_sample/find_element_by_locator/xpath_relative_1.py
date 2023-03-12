# -*- coding: utf-8 -*-
"""
Finding element by relational_XPATH
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

        Relative Xpath:
        This is always the common and preferred format used to find element as
        it is not a complete path from the root element. It starts from the
        middle of HTML DOM structure, with double forward slash (//). It can
        search elements anywhere on the webpage, means no need to write a long
        xpath, and you can start from the middle of HTML DOM structure.

        Below is a basic example of locating element by implementing
        relative-XPath expression:
"""

from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

# Pass an instance of the Service class to the Chrome class:
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://wikipedia.com")

# Find element by relational_XPATH using:
expression = "//input[@type='search']"
element = driver.find_element('xpath', expression)

print()
print(element)

element.send_keys("Hello world!")

sleep(3)

driver.quit()

