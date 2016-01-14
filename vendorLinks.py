import assertEquals as assertEquals
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from startwork import *
import unittest
import time


class vendorLinks(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://futurumshop.nl')
        self.driver.set_window_size(2000, 2000)
        time.sleep(3)

    def test_vendorLinks(self):

            self.vendorFooter = []
            top = self.driver.find_elements_by_xpath("//div[@class='hidden-xs hidden-sm row vendors inverted']/ul/li/a")
            for links in top:
                self.vendorFooter.append((str((links.get_attribute('href')))))

            for breadcrumbs in range(0, len(self.vendorFooter)):
                self.driver.get(self.vendorFooter[breadcrumbs])

                #if len(self.driver.find_elements(By.XPATH, "//ul[@class='col-xs-12']/li")) == 0:
                if self.driver.title in 'Futurumshop | Specialist in Fietsen,Hardlopen,Buitensport':
                    print self.vendorFooter[breadcrumbs],'empty url'



    def tearDown(self):
        self.driver.quit()