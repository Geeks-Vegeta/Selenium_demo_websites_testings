from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.select import Select


driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))

driver.get('https://testpages.herokuapp.com/styled/basic-html-form-test.html')

# sending creds to username
driver.find_element("xpath", "//input[@name='username']").send_keys("shreyas mohite")
# password
driver.find_element("xpath", "//input[@name='password']").send_keys("jhoncena")
# clear comments in placeholder
driver.find_element("xpath", "//textarea[@name='comments']").clear()
# adding comments in textarea
driver.find_element("xpath", "//textarea[@name='comments']").send_keys("hey jhon")
# sending images in file
driver.find_element("xpath", "//input[@type='file']").send_keys("/home/shreyas/Downloads/image.jpeg")
# selecting checkbox
driver.find_element("xpath", "//input[@value='cb1']").click()
# selecting 2 radio button with value
driver.find_element("xpath", "//input[@value='rd2']").click()

# mulitple selection
multiple_selection = Select(driver.find_element("xpath", "//select[@multiple='multiple']"))
multiple_selection.select_by_index(1)

# dropdown selection
dropdown_selection = Select(driver.find_element("xpath", "//select[@name='dropdown']"))
dropdown_selection.select_by_index(2)

# clicking on submit button
driver.find_element("xpath", "//input[@type='submit']").click()