from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Button_from_fo import *
import unittest
import random
import time


class start_webdriver():


    def openbrowser(self):
        self.driver = webdriver.Chrome()
        self.driver.get(urlNL)
        self.driver.maximize_window()

    def openbrowserDE(self):
        self.driver = webdriver.Chrome()
        self.driver.get(urlDE)
        self.driver.maximize_window()

    def start_and_login(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get(urlNL)
        self.driver.maximize_window()
        self.product = []
        products = self.driver.find_elements(By.XPATH, "//li[@class='row product']")
        for item in products:
	        self.product.append(item.get_attribute('id'))
        self.driver.find_element_by_xpath("//a[@class='loginLink']").click()
        time.sleep(2)
        logname = self.driver.find_element_by_xpath("//input[@id='regid']")
        logname.send_keys("futurumshop123@gmail.com")
        password = self.driver.find_element(By.ID, "password")
        password.send_keys("zxczxc", Keys.ENTER)

    def start_work_DE(self):
        self.driver = webdriver.Chrome()
        self.driver.get(urlDE)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.product = []
        products = self.driver.find_elements(By.XPATH, "//li[@class='row product']")
        for item in products:
	        self.product.append(item.get_attribute('id'))
        self.driver.find_element_by_xpath("//a[@class='loginLink']").click()
        time.sleep(2)
        logname = self.driver.find_element_by_xpath("//input[@id='regid']")
        logname.send_keys("futurumshop123@gmail.com")
        password = self.driver.find_element(By.ID, "password")
        password.send_keys("qwe123", Keys.ENTER)


    def click_by_xpath(self, xpath):
        self.driver.find_element(By.XPATH, xpath).click()


    def click_by_id(self, id):
        self.driver.find_element_by_id(id).click()


    def send_keys_id(self, id, value):
        self.driver.find_element(By.ID, id).send_keys(value, Keys.ENTER)


    def send_keys_xpath(self, xpath, value):
        self.driver.find_element(By.XPATH, xpath).send_keys(value, Keys.ENTER)


    def find_xpath(self, xpath):
        self.driver.find_element(By.XPATH, xpath)

    def find_xpaths(self, xpath):
        self.driver.find_elements(By.XPATH, xpath)

    def clear(self, id):
        self.driver.find_element(By.ID, id).clear()



