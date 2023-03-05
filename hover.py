from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://testpages.herokuapp.com/styled/csspseudo/css-hover.html")

# ActionChains(driver).move_to_element(
#     driver.find_element("xpath", "//p[@id='hoverpara']")).perform()

# print(driver.find_element("xpath", "//p[@id='hoverparaeffect']").text)


ActionChains(driver).move_to_element(
    driver.find_element("xpath", "//p[@id='hoverdivpara']")).perform()

driver.find_element("xpath", "//a[@id='hoverlink']").click()

