import time
from selenium import webdriver
# import os


class RunChromeTestWindows:
    def testy(self):
        driverLocation = "C:\\Users\DK\\Documents\\P\\chromedriver.exe"
        # os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(executable_path=driverLocation)
        driver.get("http://www.letskodeit.com")
        time.sleep(1505) # Let the user actually see something!

chromeTest = RunChromeTestWindows()
chromeTest.testy()
