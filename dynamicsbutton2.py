from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://testpages.herokuapp.com/styled/dynamic-buttons-disabled.html")

driver.implicitly_wait(10)
driver.find_element("xpath", "//button[@id='button00']").click()
driver.find_element("xpath", "//button[@id='button01']").click()
driver.find_element("xpath", "//button[@id='button02']").click()
driver.find_element("xpath", "//button[@id='button03']").click()