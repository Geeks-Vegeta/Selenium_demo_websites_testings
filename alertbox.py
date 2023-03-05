from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.select import Select


driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))


# alert

driver.get("https://testpages.herokuapp.com/styled/alerts/alert-test.html")
driver.find_element("xpath", "//input[@id='alertexamples']").click()
alert_popup = driver.switch_to.alert
print(alert_popup.text)
alert_popup.accept()


# confirm

# driver.find_element("xpath", "//input[@id='confirmexample']").click()
# confirm_popup = driver.switch_to.alert
# print(confirm_popup.text)
# confirm_popup.accept()


#prompt

# driver.find_element("xpath", "//input[@id='promptexample']").click()
# propmt_popup = driver.switch_to.alert
# propmt_popup.send_keys("shreyas")
# propmt_popup.accept()

