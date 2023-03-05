from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://testpages.herokuapp.com/styled/key-click-display-test.html")
driver.find_element("xpath", "//input[@id='button']").click()
driver.find_element("xpath", "//input[@id='button']").click()
