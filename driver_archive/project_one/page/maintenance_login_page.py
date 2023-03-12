from driver_archive.project_two.locator import *


class MaintenanceLoginPage:
    """
    This class is a code template for representing new objects (the main-page)
    under test. This is the page user ends up right after clicking
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

    def check_validity_of_maintenance_page(self):
        """
        Checks if webdriver ends up
        on the main page right.

        :return:
            none.
        """

        strategy = 'xpath'
        target = "//h6[contains(@class,'oxd-text oxd-text--h6')]"
        element = self.driver.find_element(strategy, target)

        return element.text
