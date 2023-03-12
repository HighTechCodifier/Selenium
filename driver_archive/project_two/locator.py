"""
This file contains locators related to
the pages under test in project_one
"""

username_textbox_NAME = 'username'
username_textbox_by_XPATH = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input'
password_textbox_NAME = 'password'

login_button_TAGNAME = 'button'

login_text_TAG_NAME = 'h5'
login_text_css_selector_based = 'div#app>div>div>div>div>div:nth-of-type(2)>h5'

dashboard_TAG_NAME = 'h6'

user_drop_down_icon_XPATH_class_based = "//i[contains(@class,'oxd-icon bi-caret-down-fill')]"
user_drop_down_icon_css_selector_based = "div#app>div>div>header>div>div:nth-of-type(2)>ul>li>span>i"

logout_XPATH_attribute_based_href = "//a[@href='/web/index.php/auth/logout']"
logout_css_selector = "div#app>div>div>header>div>div:nth-of-type(2)>ul>li>ul>li:nth-of-type(4)>a"
logout_link_text = 'Logout'
logout_XPATH_absolute = "//div[@id='app']/div[1]/div[1]/header[1]/div[1]/div[2]/ul[1]/li[1]/ul[1]/li[4]/a[1]"

# A collection of selector options to find the text 'Invalid credentials' on the login page if login fails:
invalid_credentials_message_xpath_class_based = "//p[contains(@class,'oxd-text oxd-text--p')]"
invalid_credentials_message_xpath_text_based = '//p[text()="Invalid credentials"]'
invalid_credentials_message_css_selector_based = 'div#app>div>div>div>div>div:nth-of-type(2)>div:nth-of-type(' \
                                                 '2)>div>div>div>p'


