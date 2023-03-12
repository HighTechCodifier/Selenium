# -*- coding: utf-8 -*-
"""
Finding element by a unique tag:
    Description:
        A tag name is a part of a DOM structure where every element on a page
        is being defined via tag like input tag, button tag or anchor tag etc.
        Each tag has multiple attributes like ID, name, value class etc. As
        far as other locators in Selenium are concerned, we used these
        attributes values of the tag to locate elements. In the case of tag
        name Selenium locator, we will simply use the tag name to identify an
        element.

        Please note: In a simple basic scenario where an element is located
        just via tag, it may lead to a lot of values being identified and may
        cause issues. In this case, Selenium will select or locate the first
        tag that matches the one provided from your end. So, refrain yourself
        from using tag name locator in Selenium if you intend to locate a
        single element.

        Below is a basic example of locating element by implementing a unique
        tag-name:
"""

from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

object_1 = ChromeDriverManager().install()
# Pass an instance of the Service class to the Chrome class:
driver = webdriver.Chrome(service=ChromeService(object_1))

driver.get("http://wikipedia.com")

# Find element by implementing a unique tag-name:
element = driver.find_element('tag name', 'select')

sleep(3)

element.click()

# expected_value = 'searchLanguage'
#
# try:
#     # Assertion of a certain element's text:
#     assertTrue(element.is_selected())
#     print('Assertion test passed')
#     sign_2 = True
#
# except Exception as e:
#     print('Assertion test #2 failed')

sleep(3)

driver.quit()
