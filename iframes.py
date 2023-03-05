from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))

driver.get('https://testpages.herokuapp.com/styled/iframes-test.html')

driver.switch_to.frame(driver.find_element("xpath","//iframe[@id='thedynamichtml']"))
frame_line = driver.find_element("xpath", "//li[@id='iframe0']")
print(frame_line.text)

# switching to default
driver.switch_to.default_content()


driver.switch_to.frame(driver.find_element("xpath", "//iframe[@id='theheaderhtml']"))
para_line = driver.find_element("xpath", "//div[@class='explanation']/p")
print(para_line.text)
driver.quit()