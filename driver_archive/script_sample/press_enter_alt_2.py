
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
driver.get("https://google.com")

sleep(2)

# Find element by its id:
driver.find_element("id", 'W0wltc').click()

# Send the ‘search keywords’ to the Search Bar:
driver.find_element('name', 'q').send_keys('wikipedia')

# Use XPath to access the Search Bar:
path = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]'
driver.find_element('xpath', path).click()

sleep(2)

driver.quit()    #Teardown



