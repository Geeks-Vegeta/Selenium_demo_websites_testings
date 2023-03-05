from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://testpages.herokuapp.com/styled/events/javascript-events.html")

ActionChains(driver).click(
    driver.find_element("xpath", "//button[@id='onclick']")).perform()

ActionChains(driver).double_click(
    driver.find_element("xpath", "//button[@id='ondoubleclick']")).perform()