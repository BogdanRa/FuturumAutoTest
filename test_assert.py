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
        Inlog = self.driver.find_element(By.XPATH, "//a[contains(text(), 'Inloggen')]")

        assert 'Inloggen' == Inlog.text



    def tearDown(self):
        self.driver.quit()