from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get('http://google.com')
#Firefox Webdriver is created and navigated to google.

elem = driver.find_element_by_name('q')
elem.send_keys('hey', Keys.RETURN)
#Keys.RETURN = Pressing Enter key on keyboard

time.sleep(5)
driver.close()
