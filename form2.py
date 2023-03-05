from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.color import Color
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))


driver.get("https://testpages.herokuapp.com/styled/html5-form-test.html")

driver.find_element("xpath", "//input[@name='colour']").send_keys('#2F7ED8')

datepicker=driver.find_element("xpath", "//input[@name='date']")
# ActionChains(driver).move_to_element(datepicker).click().send_keys('12292000').perform()
datepicker.send_keys('12292000')
driver.find_element("xpath", "//input[@name='email']").clear()
driver.find_element("xpath", "//input[@name='email']").send_keys("shreyas123@gmail.com")
driver.find_element("xpath", "//input[@name='month']").send_keys("December")
driver.find_element("xpath", "//input[@name='number']").clear()
driver.find_element("xpath", "//input[@name='number']").send_keys(28)
driver.find_element("xpath", "//input[@type='submit']").click()