from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time

driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://testpages.herokuapp.com/styled/javascript-redirect-test.html")

# redirect 2 seconds
#driver.find_element("xpath", "//button[@id='delaygotobounce']").click()
# driver.implicitly_wait(1)
#time.sleep(3)
#print(driver.find_element("xpath", "//div[@class='explanation']/p").text)



# redirect 5 seconds
driver.find_element("xpath", "//button[@id='delaygotobasic']").click()
# driver.implicitly_wait(1)
time.sleep(6)
print(driver.find_element("xpath", "//div[@class='explanation']/p").text)

driver.quit()


# implicit wait does not work with redirect