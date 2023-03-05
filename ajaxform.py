from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.select import Select


driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))


driver.get("https://testpages.herokuapp.com/styled/basic-ajax-test.html")



combo_select = Select(driver.find_element("xpath", "//select[@id='combo1']"))
combo_select.select_by_index(0)

driver.implicitly_wait(5)


language_select = Select(driver.find_element("xpath", "//select[@id='combo2']"))
language_select.select_by_index(2)



# combo_select = Select(driver.find_element("xpath", "//select[@id='combo1']"))
# combo_select.select_by_index(1)

# driver.implicitly_wait(5)


# language_select = Select(driver.find_element("xpath", "//select[@id='combo2']"))
# language_select.select_by_value('11')


# combo_select = Select(driver.find_element("xpath", "//select[@id='combo1']"))
# combo_select.select_by_index(2)

# driver.implicitly_wait(5)


# language_select = Select(driver.find_element("xpath", "//select[@id='combo2']"))
# language_select.select_by_value('22')
