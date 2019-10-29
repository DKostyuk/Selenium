from selenium import webdriver
from urllib.request import urlretrieve
from selenium.webdriver.common.keys import Keys
from openpyxl import Workbook
import time


class FindByIdName():

    def test(self):
        # baseUrl = "https://elmy.ua/yourbeautyagent?category=makeup-application"
        baseUrl = "https://elmy.ua/TatyanaDobryak"

        driver = webdriver.Firefox()
        driver.maximize_window()  # For maximizing window
        driver.get(baseUrl)
        driver.implicitly_wait(10)  # gives an implicit wait for 10 seconds


        try:
            elementByXpath = driver.find_elements_by_css_selector("div.service")
            print(len(elementByXpath))
            for a in elementByXpath:
                try:
                    service_name = a.find_element_by_class_name("title")
                    service_name_text = service_name.get_attribute("textContent")
                except:
                    service_name_text = "service_name.text--- NO"
                try:
                    service_price = a.find_element_by_class_name("price")
                    service_price_text = service_price.get_attribute("textContent")
                except:
                    service_price_text = "service_price.text -- NO"
                try:
                    service_duration = a.find_element_by_class_name("duration")
                    service_duration_text = service_duration.get_attribute("textContent")
                except:
                    service_duration_text = "service_duration.text -- NO"
                # try:
                #     service_more = elementByXpath.find_element_by_class_name("more")
                #     service_more.click()
                # except:
                #     service_more_text = "service_more.text -- NO more link"
                try:
                    service_description = a.find_element_by_class_name("desc")
                    service_description_text = service_description.get_attribute("textContent")
                    service_description_text = service_description_text.replace('\n', ' ')
                    while service_description_text.find('  ') != -1:
                        service_description_text = service_description_text.replace('  ', ' ')
                    service_description_text = service_description_text.split()
                    if service_description_text[0] == 'Еще':
                        service_description_text.pop(0)
                    service_description_text = ' '.join(service_description_text)
                except:
                    service_description_text = "service_description.text -- NO"

                try:
                    service_img = a.find_element_by_tag_name("img")
                    service_img_url = service_img.get_attribute("src")
                    service_img_url = service_img_url.replace('h_48', 'h_188')
                    service_img_url = service_img_url.replace('w_77', 'w_302')
                    img_service_filename = service_name_text + ".png"
                    urlretrieve(service_img_url, img_service_filename)
                except:
                    service_img_url = "service_IMAGE.url -- NO"\

                print('Service name  ------', service_name_text)
                print('Service price  ------', service_price_text)
                print('Service duration  ------', service_duration_text)
                print('Service description  ------', service_description_text)
                print('Service img_url  ------', service_img_url)

        except:
            service_Cosmo_text = "NO_TEXT_1"
            print(service_Cosmo_text)


        driver.close()
        print('END_2----')


ff = FindByIdName()
ff.test()