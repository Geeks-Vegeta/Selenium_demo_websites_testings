from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://testpages.herokuapp.com/styled/file-upload-test.html")

driver.find_element("xpath", "//input[@type='file']").send_keys("/home/shreyas/Downloads/image.jpeg")
driver.find_element("xpath", "//input[@value='image']").click()
driver.find_element("xpath", "//input[@type='submit']").click()