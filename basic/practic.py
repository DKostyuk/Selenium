from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import win32com.client as comclt
from openpyxl import Workbook


class FindByIdName():

    def test(self):
        baseUrl = "https://elmy.ua/kiev/makeup-application"
        driver = webdriver.Firefox()
        driver.maximize_window()  # For maximizing window
        driver.get(baseUrl)
        driver.implicitly_wait(10)  # gives an implicit wait for 10 seconds

        # elementByLink = ui.WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_class_name('name'))
        elementByLink = driver.find_elements_by_class_name("name")
        length_List = len(elementByLink)
        print(length_List)

        actionChains = ActionChains(driver)


        # Save the window opener (current window, do not mistaken with tab... not the same)
        # main_window = driver.current_window_handle

        if elementByLink is not None:
            # k = 1
            # for i in elementByLink:
            #     i.click()
            #     k += 1
            # print("We found an element by Link", k)
            # print('---', i)
            my_list = []
            # print('---', elementByLink[0])

            # OPEN new window

            # Open the link in a new tab by sending key strokes on the element
            # Use: Keys.CONTROL + Keys.SHIFT + Keys.RETURN to open tab on top of the stack
            # elementByLink[0].send_keys(Keys.CONTROL + Keys.SHIFT + Keys.RETURN)
            actionChains = ActionChains(driver)
            # actionChains.context_click(elementByLink[0]).send_keys("T").perform()
            wsh = comclt.Dispatch("WScript.Shell")
            # ActionChains(driver).move_to_element(element).context_click().perform()



            actionChains.context_click(elementByLink[0]).perform()
            wsh.SendKeys("{DOWN}")  # send the keys you want
            wsh.SendKeys("{ENTER}")  # send the keys you want
            driver.implicitly_wait(10)
            driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
            # driver.switch_to.window(main_window)
            # driver.implicitly_wait(3)
            actionChains.send_keys(Keys.CONTROL + Keys.TAB).perform()


            # elementByLink[0].click()
            driver.implicitly_wait(20)

            imgCosmo = driver.find_element_by_xpath("//div[@class='avatar-cont']/img")
            if imgCosmo is not None:
                print("We found an element by XPATH")

            nameCosmo_url = imgCosmo.get_attribute("src")
            print('Image URL  ------', nameCosmo_url)
            my_list.append(nameCosmo_url)

            nameCosmo = driver.find_element_by_xpath("//div[@class='name']/h2")
            nameCosmo_text = nameCosmo.text
            print('NAME ------', nameCosmo_text)
            my_list.append(nameCosmo_text)

            desCosmo = driver.find_element_by_id('service_desc_about')
            desCosmo_text = desCosmo.text
            print('desCosmo_TEXT ----', desCosmo_text)

            my_list.append(desCosmo_text)

            wb = Workbook()
            ws = wb.active
            file_name = "008_file.xlsx"

            ws.append(my_list)
            wb.save(file_name)

            # my_file = open("000_file.txt", "w")

            wb.close()


        # elementByName = driver.find_element_by_name("show-hide")
        #
        # if elementByName is not None:
        #     print("We found an element by Name")

ff = FindByIdName()
ff.test()
