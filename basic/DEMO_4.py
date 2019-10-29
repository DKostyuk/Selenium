from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from openpyxl import Workbook
import time
from urllib.request import urlretrieve


class FindByIdName():

    def test(self):
        # baseUrl = "https://elmy.ua/yourbeautyagent?category=makeup-application"
        baseUrl = "https://elmy.ua/TatyanaDobryak"

        driver = webdriver.Firefox()
        driver.maximize_window()  # For maximizing window
        driver.get(baseUrl)
        driver.implicitly_wait(10)  # gives an implicit wait for 10 seconds

        cosmo_phone_text ="ХЗ"
        try:
            cosmo_phone = driver.find_element_by_css_selector("div>a.phone-call")
            cosmo_phone_text = cosmo_phone.get_attribute("outerHTML")
            cosmo_phone_text = cosmo_phone_text[(cosmo_phone_text.find('+380')):(cosmo_phone_text.find('+380') + 13)]
        except:
            cosmo_phone_text = "cosmo_phone.text--- NO"

        print('Cosmo phone  ------', cosmo_phone_text)

        driver.close()
        print('END_2----')


ff = FindByIdName()
ff.test()