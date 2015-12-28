from startwork import start_webdriver
from selenium.common.exceptions import NoSuchElementException, UnexpectedAlertPresentException
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import random
from  Button_from_fo import *
import time




class test_order_nl(unittest.TestCase, start_webdriver):

    def setUp(self):

        # prepare browsing and webdriver for work
        self.start_and_login()

        # done
        

        self.paymethodnl = {"ideal":[ "ABNANL2A",  "RABONL2U", "INGBNL2A", "KNABNL2H", "SNSBNL2A", "RBRBNL21", "ASNBNL21", "TRIONL2U"],
                          "paypal": 'paypal', "ogonestd":["visa", "aexpress", "mastercard"],"overboeking": 'overboeking', "rmbrs": 'rmbs', "mistercash": 'mistercash'}

        #self.paymethod = {"ideal":[ "ABNANL2A",  "RABONL2U", "INGBNL2A", "KNABNL2H", "SNSBNL2A", "RBRBNL21", "ASNBNL21", "TRIONL2U", "FVLBNL22"],"paypal": 'paypal',
        #                  "ogonestd":["visa", "aexpress", "mastercard"], "overboeking": 'overboeking', "rmbrs": 'rmbs', "mistercash": 'mistercash'}



        self.ran = random.randrange(2, 8)
       

    def test_ordernl(self):


        for pmname in self.paymethodnl:

            for x in range(0, self.ran):
            #add card

                time.sleep(2)
                self.send_keys_id(search, (random.choice(self.product)))
                time.sleep(2)
                self.click_by_xpath(add_to_card)


            # steps PM
            self.click_by_xpath(go_card)
            time.sleep(2)
            self.click_by_xpath(two_step_in_card)
            time.sleep(2)
            self.click_by_id(choose_default)
            time.sleep(2)
            self.click_by_xpath(go_pm_page)
            





            if pmname == "ideal":
                for pmideal in self.paymethodnl[pmname]:
                    self.driver.get("http://futurumshop.nl")
                    time.sleep(2)
                    self.send_keys_id(search, (random.choice(self.product)))
                    time.sleep(2)
                    self.click_by_xpath(add_to_card)
                    time.sleep(2)
                    self.click_by_xpath(go_card)
                    time.sleep(2)
                    self.click_by_xpath(two_step_in_card)
                    time.sleep(2)
                    self.click_by_id(choose_default)
                    time.sleep(2)
                    self.click_by_xpath(go_pm_page)
                    time.sleep(2)
                    idealss = self.driver.find_element(By.XPATH, "//select[@id='parentId-ideal']")
                    Select(idealss).select_by_value('{}'.format(pmideal))
                    time.sleep(2)
                    print("begin")
                    self.click_by_xpath(buy_button)
                    time.sleep(2)
                    self.click_by_xpath("//button[@class='btncta icon buy large checkout pull-right']")
                    time.sleep(2)
                    self.driver.get("http://futurumshop.nl")









            elif pmname == 'ogonestd':

                for pmogonestd in self.paymethodnl[pmname]:
                    self.driver.get("http://futurumshop.nl")
                    time.sleep(2)
                    self.send_keys_id(search, (random.choice(self.product)))
                    time.sleep(2)
                    self.click_by_xpath(add_to_card)
                    time.sleep(2)
                    self.click_by_xpath(go_card)
                    time.sleep(2)
                    self.click_by_xpath(two_step_in_card)
                    time.sleep(2)
                    self.click_by_id(choose_default)
                    time.sleep(2)
                    self.click_by_xpath(go_pm_page)
                    time.sleep(2)
                    self.click_by_id('ogonestd')
                    time.sleep(2)
                    ogone = self.driver.find_element(By.XPATH, "//select[@id='parentId-ogonestd']")
                    Select(ogone).select_by_value('{}'.format(pmogonestd))
                    time.sleep(2)
                    print("begin")
                    self.click_by_xpath(buy_button)
                    time.sleep(2)
                    self.click_by_xpath("//button[@class='btncta icon buy large checkout pull-right']")
                    time.sleep(2)
                    self.driver.get("http://futurumshop.nl")



            else:
                    time.sleep(2)
                    print (pmname)
                    self.click_by_xpath("//input[@id='{}']".format(pmname))
                    time.sleep(2)
                    self.click_by_xpath(buy_button)
                    time.sleep(2)
                    self.click_by_xpath("//button[@class='btncta icon buy large checkout pull-right']")
                    time.sleep(2)
                    self.driver.get("http://futurumshop.nl")











    #def tearDown(self):
    #    self.driver.quit()
