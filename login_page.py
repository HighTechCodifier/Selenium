
from driver_archive.project_two.locator import *
from driver_archive.project_two import valid_credentials
from driver_archive.project_two import invalid_credentials


class LoginPage:
    """
    This class is a code template for representing new objects (the login-page)
    under test. This is the page users try to login to using their credentials.
    The class file only contains corresponding web page elements. Using these
    elements, testers can perform operations on the
    website under test. The objects of this will be created using a constructor
    of this class:



        This class is a code template for representing new objects for
        login-elements of a page under test.
        They will be created using
        a constructor of this class:
            ¤  __init__(self , driver)

        "self" is a keyword which represents the instance of this class.
        By using it one can access the attributes as well as the methods
        of the class.

        The Objects have a member variable (attribute):
            ¤  driver

        The also have a behaviour associated with them. It's represented
        by a method:
            ¤  enter_username(self, username)
            ¤  enter_password(self, password)
            ¤  click_on_login_button(self)
    """

    def __init__(self, driver):
        """
        Here, elements of page are defined as
        attributes of the class.
        "self" is a keyword which represents
        the instance of this class. By using
        it one can access the attributes as
        well as the methods of the class.

        :param driver:
        """
        # Define page's attributes (elements):
        self.driver = driver

    ###########################################################################

    def enter_username(self, username):
        """
        This function enters username in
        the text-box of the username on
        the page.

        :param username:
            it'll be input by user
        :return:
              none.
        """

        # Find element of username-textbox:
        strategy = 'name'
        target = username_textbox_NAME
        element = self.driver.find_element(strategy, target)

        # Enter username:
        element.send_keys(username)

    ###########################################################################

    def enter_password(self, password):
        """
        This function enters password in
        the text-box of the password on
        the page.

        :param password:
            it'll be input by user.
        :return:
            none.
        """

        # Find element of password-textbox:
        strategy = 'name'
        target = password_textbox_NAME
        element = self.driver.find_element(strategy, target)

        # Enter password
        element.send_keys(password)

    ###########################################################################

    def click_on_login_button(self):
        """
        This function clicks on the login button
        on the page.

        :return:
              none.
        """

        # Find login-button's element:
        strategy = 'tag name'
        target = login_button_TAGNAME
        element = self.driver.find_element(strategy, target)

        # Click on login-button:
        element.click()

    ###########################################################################

    def check_validity_of_login_page(self):
        """
        Checks if webdriver is on the login
        page.

        :return:
            the text 'Invalid credentials'
        """

        # Find Login-text's element
        strategy = 'tag name'
        target = login_text_TAG_NAME
        element = self.driver.find_element(strategy, target)

        return element.text

    ###########################################################################

    def check_appearance_of_invalid_credentials(self):
        """
        Checks appearance of invalid credentials on
        the login page.

        :return:
            the text 'Invalid credentials'
        """

        """
        NOTE!
        Here is collection of selector options to find the text 
        'Invalid credentials' on the login page if login fails:
                
        strategy_xpath_class_based = "//p[contains(@class,'oxd-text oxd-text--p')]"
        strategy_xpath_text_based = '//p[text()="Invalid credentials"]'
        strategy_css_selector_based = 'div#app>div>div>div>div>div:nth-of-type(2)' \
                                      '>div:nth-of-type(2)>div>div>div>p'
        """

        # Find element of invalid_credentials message:
        strategy = 'css selector'
        target = invalid_credentials_message_css_selector_based
        element = self.driver.find_element(strategy, target)

        return element.text

    ###########################################################################

    def login_to_page_with_valid_credentials(self):
        """
        Logs in to page, which is under test, with
        "Valid" credentials.

        :return:
            none.
        """

        # Login to the page using credentials:
        self.enter_username(valid_credentials.username)
        self.enter_password(valid_credentials.password)
        self.click_on_login_button()

    ###########################################################################

    def login_to_page_with_invalid_credentials(self):
        """
        Logs in to page, which is under test, with
        "Invalid" credentials.

        :return:
            none.
        """

        # Login to the page using credentials:
        self.enter_username(invalid_credentials.invalid_username)
        self.enter_password(invalid_credentials.invalid_password)
        self.click_on_login_button()
