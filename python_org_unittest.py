import unittest

"""Provides the framework for organizing the test cases"""

from selenium import webdriver

"""Provides all WebDriver implementations
    Firfox, Chrome, Ie and Remote"""

from selenium.webdriver.common.keys import Keys

""" Key class provides keys in the keyboard like
    RETURN, F1, ALT etc."""

class PythonOrgSearch(unittest.TestCase):

    """test case class is inherited from unittest.TestCase"""

    def setUp(self):

        """this method (setUp) will get called before every
            test function which you are going to write in
            the test case class"""

        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):

        """The test case method should always start with
            characters test."""

        driver = self.driver

        """Create a local reference to the driver object
        created in setUp method."""

        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def tearDown(self):

        """ will get called after every test method
        This is a place to do all cleanup actions."""

        self.driver.close()


#Run the unit test
if __name__ == "__main__":
    unittest.main()