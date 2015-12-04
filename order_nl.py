from startwork import start_webdriver
from selenium.common.exceptions import NoSuchElementException, UnexpectedAlertPresentException
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import random
#from  connect_to_bd import self.product_form_bd
from Button_from_fo import *
import time


class test_order_nl(unittest.TestCase, start_webdriver):

    def setUp(self):

        # prepare browsing and webdriver for work
        self.start = start_webdriver()
        self.driver = self.start.start_and_login()
        self.xpath = self.start.click_by_xpath
        self.click_by_id = self.start.click_by_id
        self.send_to_id = self.start.send_keys_id
        self.send_to_xpath = self.start.send_keys_xpath

        # done

        self.paymethodnl = {"ideal":[ "ABNANL2A",  "RABONL2U", "INGBNL2A", "KNABNL2H", "SNSBNL2A", "RBRBNL21", "ASNBNL21", "TRIONL2U", "FVLBNL22"]}#,
                          #"paypal": 'paypal', "ogonestd":["visa", "aexpress", "mastercard"],"overboeking": 'overboeking', "rmbrs": 'rmbs', "mistercash": 'mistercash'}






        self.ran = random.randrange(2, 8)


        # add self.products ( connect to mysql )
        #self.products = self.product_form_bd()
        #self.product = self.products.connect_to_mysql()
        # close connect :)

        self.product = ["6004-0577-001-N1502", "6040-0063-001-N1405", "6282-0017-N1109",
                   "6124-0012-N0610","6422-0002-N1309", "6308-0124-N1410",
                   "6119-0290-N1407", "9087026"]


    def test_ordernl(self):


        for pmname in self.paymethodnl:

            for x in range(0, self.ran):
            #add card
                try:
                    time.sleep(2)
                    self.send_to_id(search, (random.choice(self.product)))

                except UnexpectedAlertPresentException:
                    self.driver.switch_to_alert().accept()

                time.sleep(1)

                self.xpath(add_to_card)
                print("Add to card " + random.choice(self.product))

            # steps PM
            self.xpath(go_card)
            time.sleep(2)
            self.xpath(two_step_in_card)
            time.sleep(2)
            self.click_by_id(choose_default)
            time.sleep(2)
            self.xpath(go_pm_page)
            time.sleep(2)





            if pmname == "ideal":
                for pmideal in self.paymethodnl[pmname]:
                    time.sleep(2)
                    Select(self.xpath( "//input[@id='ideal']")).select_by_value('{}'.format(pmideal))

                    time.sleep(2)
                    print("begin")
                    time.sleep(2)
                    self.xpath(buy_button)
                '''
                    self.send_to_id(search, (random.choice(self.product)))
                    time.sleep(2)
                    self.xpath(add_to_card)
                    #steps PM
                    time.sleep(2)
                    self.xpath(go_card)
                    time.sleep(2)
                    self.xpath(two_step_in_card)
                    time.sleep(2)
                    self.click_by_id(choose_default)
                    time.sleep(2)
                    self.xpath(go_pm_page)
                    Select(self.driver.find_element(By.ID, "parentId-ideal")).select_by_value('{}'.format(pmideal))
                    time.sleep(2)
                    self.xpath(buy_button)
                    #self.driver.get("http://futurumshop.nl")










            elif pmname == 'ogonestd':

                for pmogonestd in self.paymethodnl[pmname]:

                    self.send_to_id(search, (random.choice(self.product)))
                    self.xpath(add_to_card)
                    #steps PM
                    self.xpath(go_card)
                    self.xpath(two_step_in_card)
                    self.click_by_id(choose_default)
                    self.xpath(go_pm_page)

                    Select(self.driver.find_element_by_id("parentId-ideal")).select_by_value('{}'.format(pmogonestd))
                    self.xpath(buy_button)



            else:

                    self.xpath("//input[@id='{}']".format(pmname))
                    self.xpath(buy_button)
                    #self.driver.get("http://futurumshop.nl")

            '''









   # def tearDown(self):
   #     self.driver.quit()
