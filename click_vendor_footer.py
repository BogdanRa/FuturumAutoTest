from selenium import webdriver
import unittest
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# If breadcrumps ==  0 or 1 make screanshot with name vendor

class test_vendor(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1900, 1900)
        self.driver.get('http://testing.futurumshop.nl')

    def test_broken_linkvendor_in_footer(self):

        li = 0
        ul = 1
        self.vendor_name = []
        while li <= 83:
            try:
                li += 1
                if li == 83:
                    ul += 1
                    li = 1
                if ul == 5 and li == 2:
                    return False
                self.footer = self.driver.find_element_by_xpath("//*[@id='footer']/div[4]/ul[{}]/li[{}]/a".format(ul, li))
                self.vendor_name.append(self.footer.get_attribute('href')[26::])
                self.footer.click()



                x =  self.driver.find_elements_by_xpath("//div[@class='breadcrumb row']//li")
                if len(x) <= 1:

                    for names in self.vendor_name:
                            pass
                    self.driver.get_screenshot_as_file('/home/bohdan/{0!s}.png'.format(names))
            except NoSuchElementException:
                    self.driver.get('http://futurumshop.nl')
                    print("Lending page ")

    def tearDown(self):
        self.driver.quit()