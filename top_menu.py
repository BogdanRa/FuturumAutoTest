from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import time


class test_top_menu(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://futurumshop.nl')
        self.driver.set_window_size(2000, 2000)
        self.top_menu = []


    def test_top_menu_first_category(self):


            top = self.driver.find_elements_by_xpath("//li[@class='top_menu_element inactive']")
            for i in top:
                print(self.driver.find_element_by_tag_name(i.get_attribute('href')))



    def tearDown(self):
        self.driver.quit()