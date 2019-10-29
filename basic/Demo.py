from selenium import webdriver
import openpyxl
from urllib.request import urlretrieve
from selenium.webdriver.common.keys import Keys
from openpyxl import Workbook
import time


class FindByIdName():

    def test(self):
        baseUrl = "https://elmy.ua/kiev/makeup-application?page=3"
        driver = webdriver.Firefox()
        driver.maximize_window()  # For maximizing window
        driver.get(baseUrl)
        driver.implicitly_wait(10)  # gives an implicit wait for 10 seconds

        file_name = "001_cosmo_file.xlsx"
        wb_cosmo = openpyxl.load_workbook(file_name)
        ws_cosmo = wb_cosmo.active

        file_name_service = "001_service_file.xlsx"
        wb_service = openpyxl.load_workbook(file_name_service)
        ws_service = wb_service.active

        elementByLink = driver.find_elements_by_css_selector("div.search-item>a")

        
        name_url_list = []
        for i in range(0, len(elementByLink)):
            name_url = elementByLink[i].get_attribute("href")
            print('---', i)
            print('name_url----', name_url)
            name_url_list.append(name_url)
            i += 1
        length_List = len(elementByLink)
        print(length_List)
        print('name_url_list ---', name_url_list)
        driver.close()
        print('END_1')

        for k in name_url_list:
            my_list = []
            driver = webdriver.Firefox()
            driver.maximize_window()  # For maximizing window
            driver.get(k)
            driver.implicitly_wait(30)  # gives an implicit wait for 10 seconds

            my_list.append(k)

# -----------Start NAME------------
            try:
                nameCosmo = driver.find_element_by_class_name("name")
                nameCosmo_text = nameCosmo.text
            except:
                nameCosmo_text = 'nameCosmo ---- No name'
            print('NAME ------', nameCosmo_text)
            my_list.append(nameCosmo_text)
# ----------Finifsh Name---------------------
# -------Start IMG ------
            try:
                imgCosmo = driver.find_element_by_class_name("img")
                nameCosmo_url = imgCosmo.get_attribute("src")
                img_cosmo_filename = nameCosmo_text + ".png"
                urlretrieve(nameCosmo_url, img_cosmo_filename)
            except:
                nameCosmo_url = "nameCosmo_url--- NO"
            print('Image URL  ------', nameCosmo_url)
            my_list.append(nameCosmo_url)
# -------Finish IMG--------
# -----Start Description ------------
            try:
                desCosmo = driver.find_element_by_id('service_desc_about')
                desCosmo_text = desCosmo.text
            except:
                desCosmo_text = k
            my_list.append(desCosmo_text)
            print('desCosmo_TEXT ----', desCosmo_text)
# --------Finish Description------
# start Address--------------------------------------------------------------------------------------------------
            try:
                elementByXpath = driver.find_element_by_xpath(
                    "/html/body/section/div[2]/div/div[2]/div[2]/div[4]/div[1]/div[2]/div/span")
                addressCosmo_text = elementByXpath.text
            except:
                addressCosmo_text = "NO_TEXT_1"
            my_list.append(addressCosmo_text)

            print('Address_MAIN  ------', addressCosmo_text)

            try:
                elementByXpath = driver.find_element_by_xpath(
                    "/html/body/section/div[2]/div/div[2]/div[2]/div[4]/div[1]/div[2]/div")
                addressCosmo_text_1 = elementByXpath.text
            except:
                addressCosmo_text_1 = "NO_TEXT_2"
            my_list.append(addressCosmo_text_1)
            print('Address_2  ------', addressCosmo_text_1)

            try:
                elementByXpath_2 = driver.find_element_by_xpath(
                    "/html/body/section/div[2]/div/div[2]/div[2]/div[4]/div[1]/div[2]/div/div")
                addressCosmo_text_2 = elementByXpath_2.text
            except:
                addressCosmo_text_2 = "NO_TEXT_3"
            my_list.append(addressCosmo_text_2)
            print('Address_3  ------', addressCosmo_text_2)
# end Address --------------------------------------------------------------------------------------------
#---------------Start Schedule-------------------
            try:
                service_schedule = driver.find_elements_by_tag_name("tr")
                service_schedule_whole_text = ''
                for j in range(0, len(service_schedule)):
                    service_schedule_text = service_schedule[j].text
                    service_schedule_whole_text = service_schedule_whole_text + '\n' + service_schedule_text
                service_schedule_whole_text = service_schedule_whole_text.replace(('\n'+'Рабочий график Перерыв'+'\n'), '')

                print('Service name  ------', service_schedule_whole_text)

            except:
                service_schedule_whole_text = "service_schedule.text--- NO"
            my_list.append(service_schedule_whole_text)

            print('Service schedule  ------', service_schedule_whole_text)
# -------------Finish Schedule-------------------------
# ---------------Start Phone-------------------
            try:
                cosmo_phone = driver.find_element_by_css_selector("div>a.phone-call")
                cosmo_phone_text = cosmo_phone.get_attribute("outerHTML")
                cosmo_phone_text = cosmo_phone_text[
                                   (cosmo_phone_text.find('+380')):(cosmo_phone_text.find('+380') + 13)]
            except:
                cosmo_phone_text = "cosmo_phone.text--- NO"

            print('Cosmo phone  ------', cosmo_phone_text)
# -------------Finish Phone-------------------------
# Start --- open(see more above) and write in the file ---------------
            ws_cosmo.append(my_list)
            wb_cosmo.save(file_name)

# Finish ----- write in the file - close file -----------------

# ------Start Service---------------------


            my_list_service = [k]

            try:
                elementByXpath = driver.find_elements_by_css_selector("div.service")
                print(len(elementByXpath))
                for a in elementByXpath:
                    try:
                        service_name = a.find_element_by_class_name("title")
                        service_name_text = service_name.get_attribute("textContent")
                    except:
                        service_name_text = "service_name.text--- NO"
                    my_list_service.append(service_name_text)
                    try:
                        service_price = a.find_element_by_class_name("price")
                        service_price_text = service_price.get_attribute("textContent")
                    except:
                        service_price_text = "service_price.text -- NO"
                    my_list_service.append(service_price_text)
                    try:
                        service_duration = a.find_element_by_class_name("duration")
                        service_duration_text = service_duration.get_attribute("textContent")
                    except:
                        service_duration_text = "service_duration.text -- NO"
                    my_list_service.append(service_duration_text)
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
                    my_list_service.append(service_description_text)
                    try:
                        service_img = a.find_element_by_tag_name("img")
                        service_img_url = service_img.get_attribute("src")
                        service_img_url = service_img_url.replace('h_48', 'h_188')
                        service_img_url = service_img_url.replace('w_77', 'w_302')
                        img_service_filename = nameCosmo_text + "_" + service_name_text + ".png"
                        urlretrieve(service_img_url, img_service_filename)
                    except:
                        service_img_url = "service_IMAGE.url -- NO"
                    my_list_service.append(service_img_url)
                    print('Service name  ------', service_name_text)
                    print('Service price  ------', service_price_text)
                    print('Service duration  ------', service_duration_text)
                    print('Service description  ------', service_description_text)
                    print('Service img_url  ------', service_img_url)

            except:
                service_Cosmo_text = "NO_TEXT_1"
                print(service_Cosmo_text)

            ws_service.append(my_list_service)
            wb_service.save(file_name_service)

# -----------Finish Service--------------------

            driver.close()
            print('END_2----', k)
        wb_cosmo.close()
        wb_service.close()



ff = FindByIdName()
ff.test()