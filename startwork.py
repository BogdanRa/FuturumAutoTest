from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class start_webdriver():

    def start_and_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://futurumshop.nl")
        self.driver.set_window_size(2000, 2000)

        self.driver.find_element_by_xpath("//a[@class='loginLink']").click()
        time.sleep(2)
        logname = self.driver.find_element_by_xpath("//input[@id='regid']")
        logname.send_keys("futurumshop123@gmail.com")
        password = self.driver.find_element(By.ID, "password")
        password.send_keys("zxczxc", Keys.ENTER)


    def click_by_xpath(self, xpath):
        self.driver.find_element(By.XPATH, xpath).click()
        print("click by " + xpath)

    def click_by_id(self, id):
        self.driver.find_element_by_id(id).click()
        print("click by " + id)

    def send_keys_id(self, id, value):
        self.driver.find_element(By.ID, id).send_keys(value, Keys.ENTER)
        print("send keys to " + id)

    def send_keys_xpath(self, xpath, value):
        self.driver.find_element(By.XPATH, xpath).send_keys(value, Keys.ENTER)
        print("send keys to " + xpath)



