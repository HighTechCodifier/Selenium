from locator import *
from time import sleep

class MainPage:
    """
    This class is a code template for representing new objects (the main-page)
    under test. This is the page one ends up right after a successful login
    takes place. The class file only contains corresponding web page elements.
    Using these elements, testers can perform operations on the website under
    test. The objects of this will be created using a constructor
    of this class:
        ¤  __init__(self , driver)

    The Objects have member variables:
        ¤  driver

    The also have a behaviour associated with them. It's represented
    by a method:
        ¤  check_main_page(self)
    """

    def __init__(self, driver):
        self.driver = driver

    ###########################################################################

    def check_validity_of_main_page(self):
        """
        Checks if webdriver ends up
        on the main page right.

        :return:
            none.
        """

        strategy = 'tag name'
        target = dashboard_TAG_NAME
        self.driver.find_element(strategy, target)

    ###########################################################################

    def click_on_user_drop_down_button(self):
        """
        This function clicks on user-drop-down
        button to watch the list.

        :return:
              none.
        """
        strategy = 'css selector'
        target = 'div#app>div>div>header>div>div:nth-of-type(2)>ul>li>span>i'
        # target = user_drop_down_icon_css_selector_based
        self.driver.find_element(strategy, target).click()

    ###########################################################################

    def click_on_logout_button(self):
        """
        This function clicks on logout
        button.

        :return:
              none.
        """

        strategy = 'link text'
        target = 'Logout'
        element = self.driver.find_element(strategy, target).click()

    ###########################################################################

    def switch_to_maintenance_page(self):
        """
        switches to maintenance page

        :return:
            none.
        """

        strategy = 'xpath'
        target = "//span[text()='Maintenance']"
        self.driver.find_element(strategy, target).click()

    ###########################################################################

    def get_maintenance_text(self):
        """
        Gets the text: Maintenance

        :return:
            text: Maintenance
        """

        strategy = 'xpath'
        target = "//span[text()='Maintenance']"
        element = self.driver.find_element(strategy, target)

        return element.text

    ###########################################################################
    def go_back_to_previous_page(self):
        self.driver.back()
