from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.select import Select


driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))


driver.get("https://testpages.herokuapp.com/styled/attributes-test.html")

# name = driver.find_element("xpath", "//p[@id='domattributes']").get_attribute("original-title")
# print(name)

next_id = driver.find_element("xpath", "//p[@id='jsattributes']").get_attribute('nextid')
print(next_id)
driver.find_element("xpath", "//button[@class='styled-click-button']").click()

print(next_id)

driver.quit()