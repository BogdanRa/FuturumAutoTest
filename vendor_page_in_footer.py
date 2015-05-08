from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest






class test_vendor_page_search(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://futurumshop.nl')
        self.driver.set_window_size(2000, 2000)
        self.link_in_massive = []

    def test_footer_vendor(self):
        element = self.driver.find_elements_by_xpath("//div[@class='hidden-xs hidden-sm row vendors inverted']//a") # All vendor element in footer
        for vendor_name in element:
            self.link_in_massive.append(vendor_name.get_attribute('href')[26::])        # Get attribute vendor(http://futurumshop.nl/adidas  =[26::] = adidas
        for parse in self.link_in_massive:
            pole_search = self.driver.find_element_by_id("fc_search").send_keys(parse.replace("-", " ") + Keys.ENTER)       #Add name vendor to search

    def tearDown(self):
        self.driver.quit()

