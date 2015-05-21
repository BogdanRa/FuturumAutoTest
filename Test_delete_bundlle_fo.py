
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
import time
import unittest

# Search product on FO ( in progress )

class test_delete_bundlle_on_Fo(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://futurumshop.nl/')
        self.driver.set_window_size(1900, 1900)

    def test_bundlle_delete_on_Fo(self):
        self.bundlename = []
        bundle_delete_file = open('names', 'r')
        for i in bundle_delete_file:
          self.bundlename.append(i[8::])
        bundle_delete_file.close()


        for bundle in self.bundlename:
                 pole_search = self.driver.find_element_by_id("fc_search").send_keys(bundle)
                 x = self.driver.find_elements_by_xpath("//div[@class='breadcrumb row']//li")
                 if len(x) == 2:
                    print("Not Found " + bundle)
                 else:
                    print("On fo " + bundle)
        self.driver.quit()

    def tearDown(self):
        self.driver.quit()