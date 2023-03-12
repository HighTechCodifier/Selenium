from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

# Pass an instance of the Service class to the Chrome class:
driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

url = "https://opensource-demo.orangehrmlive.com/" \
      "web/index.php/auth/login"
driver.get(url)

driver.implicitly_wait(3)

page_url = driver.current_url

sign_1 = False
sign_2 = False

try:
    # Assertion of URL:
    assert url in page_url
    print('\nAssertion test #1 passed')
    sign_1 = True

except Exception as e:
    print('\nAssertion test #1 failed')

# Selector options to find element of Login-sing on login-page:

# By tag name:
Login_sign_by_tag_name = 'h5'

# By class name:
Login_sign_by_class_name = "orangehrm-login-title"

# By xpath:
Login_sign_by_xpath_absolute = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/h5[1]"
Login_sign_by_xpath_relative = "//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[2]/h5[1]"
Login_sign_by_xpath_class = "//h5[contains(@class,'oxd-text oxd-text--h5')]"
Login_sign_by_xpath_text = "//h5[text()='Login']"

# By css selector:
Login_sign_by_css_selector = 'div#app>div>div>div>div>div:nth-of-type(2)>h5'

element = driver.find_element('css selector', Login_sign_by_css_selector)

actual_value = element.text
expected_value = 'Login'

try:
    # Assertion of a certain element's text:
    assert actual_value == expected_value
    print('Assertion test #2 passed')
    sign_2 = True

except Exception as e:
    print('Assertion test #2 failed')

if sign_1 == True and sign_2 == True:
    print('¤¤¤¤¤¤# TEST COMPLETED ¤¤¤¤¤¤#')

sleep(3)

driver.quit()
