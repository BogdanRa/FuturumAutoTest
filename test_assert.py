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
        inlog = self.driver.find_element(By.XPATH, "//a[contains(text(), 'Inloggen')]")
        if 'Inloggen' in inlog.text:
            print ("INLOG")



    def tearDown(self):
        self.driver.quit()