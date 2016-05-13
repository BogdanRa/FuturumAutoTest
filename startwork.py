
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from Button_from_fo import *
import unittest
import random
import time


class start_webdriver():


    def openbrowser(self, urls):
        self.driver = webdriver.Chrome()
        self.driver.get(urls)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def StartAndLogin(self, urls):
        self.openbrowser(urls)
        self.product = []
        products = self.driver.find_elements(By.XPATH, "//li[@class='row product']")
        for item in products:
            if item.get_attribute('id') != '6100-0148-001-N1311':
                self.product.append(item.get_attribute('id'))
        self.driver.find_element_by_xpath("//a[@class='loginLink']").click()
        time.sleep(2)
        logname = self.driver.find_element_by_xpath("//input[@id='regid']")
        logname.send_keys("futurumshop123@gmail.com")
        password = self.driver.find_element(By.ID, "password")
        password.send_keys("zxczxc", Keys.ENTER)
        self.ran = random.randrange(2, 4) # Product in cart

    def click_by_xpath(self, xpath):

        self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        self.driver.find_element_by_xpath(xpath).click()

    def click_by_id(self, id):

        self.wait.until(EC.element_to_be_clickable((By.ID, id)))
        self.driver.find_element_by_id(id).click()


    def send_keys_id(self, id, value):
        time.sleep(2)
        #self.wait.until(EC.element_to_be_clickable((By.ID, id)))
        self.driver.find_element(By.ID, id).send_keys(value, Keys.ENTER)


    def send_keys_xpath(self, xpath, value):

        self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        self.driver.find_element(By.XPATH, xpath).send_keys(value, Keys.ENTER)


    def find_xpath(self, xpath):

        #self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        self.driver.find_element(By.XPATH, xpath)

    def find_xpaths(self, xpath):

        self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        self.driver.find_elements(By.XPATH, xpath)

    def clear(self, id):

        self.wait.until(EC.element_to_be_clickable((By.ID, id)))
        self.driver.find_element(By.ID, id).clear()

    def PINdelivery(self, delivery):
         self.click_by_xpath(go_card)
         self.click_by_xpath(two_step_in_card)
         self.click_by_id(delivery)
         self.click_by_xpath(go_pm_page)

    def verificationsteps(self): # Choose delivery and payment method
        self.click_by_xpath(go_card)
        self.click_by_xpath(two_step_in_card)
        self.click_by_id(choose_default)
        self.click_by_xpath(go_pm_page)

    def placeorder(self): # Place order on FO
        self.click_by_xpath(buy_button)
        self.click_by_xpath("//button[@class='btncta icon buy large checkout pull-right']")
        time.sleep(3)
        self.driver.get(urlNL)


    def generatecart(self): # Generate cart with products from first search page ( Default sorting )
        time.sleep(2)
        for totalproductincart in range(0, self.ran):
            self.send_keys_id(search, (random.choice(self.product)))
            self.click_by_xpath(add_to_card)

    def PMideal(self, ideal):
        idealss = self.driver.find_element(By.XPATH, "//select[@id='parentId-ideal']")
        Select(idealss).select_by_value('{}'.format(ideal))

    def PMogone(self, ogones):
        self.click_by_id('ogonestd')
        time.sleep(2)
        ogone = self.driver.find_element(By.XPATH, "//select[@id='parentId-ogonestd']")
        Select(ogone).select_by_value('{}'.format(ogones))