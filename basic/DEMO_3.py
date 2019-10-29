from selenium import webdriver
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

        my_list = []
        try:
            service_schedule = driver.find_elements_by_tag_name("tr")
            service_schedule_whole_text =''
            for j in range(0, len(service_schedule)):
                service_schedule_text = service_schedule[j].text
                service_schedule_whole_text = service_schedule_whole_text + '\n' + service_schedule_text
                print('Service name  ------', service_schedule_whole_text)
        except:
            service_schedule_whole_text = "service_schedule.text--- NO"
        my_list.append(service_schedule_whole_text)

        wb = Workbook()
        ws = wb.active
        file_name = "008_file.xlsx"
        ws.append(my_list)
        wb.save(file_name)

        print(my_list)
        print('qwerty' + '\n' + 'QWERTY')
        # print('Service name  ------', service_schedule_text)
        # print('Service name  ------', service_price_text)
        # print('Service name  ------', service_duration_text)
        # print('Service name  ------', service_description_text)
        # print('Service name  ------', service_img_url)


        driver.close()
        print('END_2----')


ff = FindByIdName()
ff.test()