from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class FindByIdName():

    def test(self):
        driver = webdriver.Firefox()
        driver.get('http://google.com')

        el = driver.find_element_by_tag_name('body')
        el.send_keys(Keys.CONTROL + 't')
        driver.get('http://bing.com')
        time.sleep(3)



ff = FindByIdName()
ff.test()
