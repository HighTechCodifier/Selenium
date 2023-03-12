"""
Description:
    This modul contains tests of the login_elements
"""

import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from driver_archive.project_two.page_URL import url
from driver_archive.project_two.page.main_page import MainPage
from driver_archive.project_two.page.login_page import LoginPage
from driver_archive.project_two.page.maintenance_login_page import MaintenanceLoginPage
from driver_archive.project_two.locator import dashboard_TAG_NAME


class LoginTest(unittest.TestCase):
    """
    This is test-class that contains all
    test-methods, setup-and teardown funcs.
    It inherits from unittest.TestCase
    """

    ###########################################################################

    @classmethod
    def setUpClass(cls) -> None:
        """
        It'll be executed only once, before
        running any test method or setUp or
        tearDown method present in the test
        Class. It should also be decorated
        with a @classmethod.

        :return:
            none
        """

        # Pass an instance of the Service class to the Chrome class:
        cls.driver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()))

        """
        Tell the webdriver to Wait maximum a certain
        amount of time for element's presence when
        trying to find an element or elements if they
        are not immediately available.
        """
        cls.driver.implicitly_wait(3)

        """
        Maximize the current window 
        that webdriver is using:
        """
        cls.driver.maximize_window()

    ###########################################################################

    """ TEST #1 """

    def test_1_homepage_is_valid(self):
        """
        Verifies whether webdriver
        (or user) have arrived to
        the correct webpage or not.

        :return:
            none.
        """

        # Open webpage:
        self.driver.get(url)

        # Read actual page-title of the page:
        actual_title = self.driver.title

        # Define the expected title of the page:
        expected_title = 'OrangeHRM'

        # Assert page-title:
        assert actual_title == expected_title

    ###########################################################################

    """ TEST #2 """

    def test_2_invalid_login(self):
        """
        Tests functionality of login-elements of the page
        with invalid credentials.

        :return:
            none.
        """

        # Create an object in the class Login:
        login_page_object = LoginPage(self.driver)

        # Login to the page using "Invalid" credentials:
        login_page_object.login_to_page_with_invalid_credentials()

        # Control validity of login page:
        login_page_object.check_validity_of_login_page()

        # Find displayed message:
        actual_value = login_page_object. \
            check_appearance_of_invalid_credentials()

        expected_value = 'Invalid credentials'

        # Assertion of a certain element's text:
        assert actual_value == expected_value

        sleep(3)

    ###########################################################################

    """ TEST #3 """

    def test_3_valid_login(self):
        """
        Tests functionality of
        login-elements of the
        page with valid
        credentials

        :return:
            none.
        """

        # # Open webpage:
        # self.driver.get(url)
        # Login to the page:
        # self.login_to_page()

        # Create an object in the class Login:
        login_page_object = LoginPage(self.driver)
        login_page_object.login_to_page_with_valid_credentials()

        # Create an object in the class MainPage:
        main_page_object = MainPage(self.driver)

        main_page_object.check_validity_of_main_page()

        # Read the actual page-title:
        actual_value_of_title = self.driver.title

        # Define the expected title of the page:
        expected_value_of_title = 'OrangeHRM'

        # Assert page-title:
        assert actual_value_of_title == expected_value_of_title

        sleep(3)

    ###########################################################################

    """ TEST #4 """

    def test_4_switching_to_maintenance(self):
        """
        Switches to maintenance page from main page.

        :return:
            none
        """

        # Create an object in the class MainPage:
        main_page_object = MainPage(self.driver)

        actual_value = main_page_object.get_maintenance_text()

        expected_value = 'Maintenance'

        # Assert text (Maintenance) on main page:
        assert actual_value == expected_value

        # switch to maintenance-page:
        main_page_object.switch_to_maintenance_page()

        # Create an object in the class MaintenanceLoginPage:
        maintenance_page_object = MaintenanceLoginPage(self.driver)

        # ASSERTION:
        actual_value = maintenance_page_object. \
            check_validity_of_maintenance_page()

        expected_value = 'Administrator Access'

        # Assert text (Administrator Access) on maintenance page:
        assert actual_value == expected_value

        # Go back to previous page:
        main_page_object.go_back_to_previous_page()

    ###########################################################################

    """ TEST #5 """

    def test_5_logout(self):
        """
        Tests functionality of
        logout-element of the
        page with valid
        credentials

        :return:
            none.
        """

        # Create an object in the class MainPage:
        main_page_object = MainPage(self.driver)

        main_page_object.click_on_user_drop_down_button()
        main_page_object.click_on_logout_button()

        # Create an object in the class Login:
        login_page_object = LoginPage(self.driver)

        # ASSERTION:
        # Find the Login-text on login page:
        actual_value = login_page_object.check_validity_of_login_page()

        expected_value = 'Login'

        # Assert of Login-text on page:
        assert actual_value == expected_value

        sleep(3)

    ###########################################################################

    @classmethod
    def tearDownClass(cls) -> None:
        """
        It'll be executed after completing all
        the test methods and all in a class, i.e.
        this method will be executed just before
        exiting the class from memory. The method
        will be executed only once in the test.
        It should also be annotated as @classmethod.

        :return:
            none.
        """

        """
        Close the browser window
        currently in focus. 
        """
        cls.driver.close()

        """
        Quits the entire browser
        session with all its tabs
        and windows.
        """
        cls.driver.quit()
