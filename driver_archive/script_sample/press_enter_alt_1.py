from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# This import is related to Alt_1
from selenium.webdriver.common.keys import Keys

from time import sleep

# Pass an instance of the Service class to the Chrome class:
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

'''
Browser action 1:
navigate (open) to a page given by the URL:
'''
driver.get("https://google.com")

sleep(2)

# Find element by its id:
driver.find_element("id", 'W0wltc').click()

# Send the ‘search keywords’ to the Search Bar:
driver.find_element('name', 'q').send_keys('wikipedia')

driver.find_element('name', 'q').send_keys(Keys.RETURN)

sleep(4)

driver.quit()    # Teardown
