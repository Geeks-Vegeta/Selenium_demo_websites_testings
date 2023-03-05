from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://testpages.herokuapp.com/styled/basic-javascript-validation-test.html")


driver.find_element("xpath", "//input[@id='lteq30']").send_keys("hello shreyas")
driver.find_element("xpath", "//input[@type='submit']").click()
driver.switch_to(driver.window_handles[1])
print(driver.find_element("xpath", "//li[@id='_valuevalue']").text)