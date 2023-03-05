from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://testpages.herokuapp.com/styled/expandingdiv.html")

ActionChains(driver).move_to_element(driver.find_element("xpath", "//div[@class='expand']")).perform()
driver.find_element("xpath", "//a[contains(text(),'This link')]").click()
time.sleep(3)
print(driver.find_element("xpath", "//div[@class='noticeme']/p").text)
driver.quit()