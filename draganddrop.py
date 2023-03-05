from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://testpages.herokuapp.com/styled/drag-drop-javascript.html")


drag1 = driver.find_element("xpath", "//div[@id='draggable1']")
drop1 = driver.find_element("xpath", "//div[@id='droppable1']") 

drag2 = driver.find_element("xpath", "//div[@id='draggable2']")
drop2 = driver.find_element("xpath", "//div[@id='droppable2']") 

ActionChains(driver).drag_and_drop(drag1, drop1).perform()
ActionChains(driver).drag_and_drop(drag2, drop2).perform()
