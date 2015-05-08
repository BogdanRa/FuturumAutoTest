from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest





class test_asser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.page = self.driver.get("http://futurumshop.nl")
        self.driver.set_window_size(2000, 2000)



    def test_allarm(self):
        mass = []
        button = self.driver.find_element_by_xpath("//div[@class='input-group-addon'][2]").click()
        productlist = self.driver.find_elements_by_xpath("//ul[@class='productList']/li[@class!='bundle row']")
        for product in productlist:
            mass.append(product)
        print(len(mass))
        assert 50 == len(mass)



    def tearDown(self):
        self.driver.quit()