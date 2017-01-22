from selenium import webdriver
from selenium.webdriver.common.keys import Keys
"""The Keys class provide keys in the keyboard like RETURN, F1, ALT etc."""

driver = webdriver.Firefox()
driver.get("http://www.python.org")
"""navigate to a page given by the URL
    WebDriver will wait until the page
    has fully loaded (that is, the 'onload'
    event has fired) before returning control
    to your test or script """
assert "Python" in driver.title
"""assertion to confirm that title has "Python" word in it"""
elem = driver.find_element_by_name("q")
""" WebDriver offers a number of ways to find elements
    using one of the find_element_by_* methods
    e.g. input text
    can be located by its name attribute using find_element_by_name """
elem.clear()
""" To be safe, clear any prepopulated text in the input field (e.g Search)"""
elem.send_keys("pycon")
"""Sending keys, is similar to entering keys using your keyboard
    Special keys can be sent using Keys class imported from
    selenium.webdriver.common.keys"""
elem.send_keys(Keys.RETURN)
assert "No results result found." not in driver.page_source
""" After submission of the page, you should get the result
    if there is any.
    To ensure that some results are found, make an assertion"""
driver.close()
"""The browser window is closed"""