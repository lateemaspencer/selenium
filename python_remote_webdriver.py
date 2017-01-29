from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys

driver = webdriver.Remote(
    command_executor="http://127.0.0.1:4444/wd/hub",
    desired_capabilities=DesiredCapabilities.FIREFOX
)

driver.get("http://www.python.org")

assert "Python" in driver.title

elem = driver.find_element_by_name("q")

elem.clear()

elem.send_keys("pycon")

elem.send_keys(Keys.RETURN)
assert "No results result found." not in driver.page_source

driver.close()
