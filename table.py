from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))

driver.get('https://testpages.herokuapp.com/styled/tag/table.html')

checkboxes = driver.find_element("xpath","//td[contains(text(),'Alan')]")
number = driver.find_element("xpath", "//td[contains(text(),'12')]")
print(f"{checkboxes.text} {number.text}")
