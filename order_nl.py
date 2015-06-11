from startwork import start_webdriver
from selenium.common.exceptions import NoSuchElementException, UnexpectedAlertPresentException
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import random
#from  connect_to_bd import product_form_bd
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.support import expected_conditions as EC
from  Button_from_fo import *

class test_order_nl(unittest.TestCase):

    def setUp(self):

        # prepare browsing and webdriver for work
        self.start = start_webdriver()
        self.driver = self.start.start_and_login()
        self.xpath = self.start.click_by_xpath
        self.click_by_id = self.start.click_by_id
        self.send_to_id = self.start.send_keys_id
        self.send_to_xpath = self.start.send_keys_xpath

        # done

        self.paymethod = {"ideal":[ "FVLBNL22", "ABNANL2A",  "RABONL2U", "INGBNL2A", "KNABNL2H", "SNSBNL2A", "RBRBNL21", "ASNBNL21", "TRIONL2U"], "paypal": 'paypal', "ogonestd":["visa", "aexpress", "mastercard"],"overboeking": 'overboeking', "rmbrs": 'rmbs', "mistercash": 'mistercash'}

        self.ran = random.randrange(2, 10)




    def test_ordernl(self):


        product = ["6003-0072-N1011"]
        # add products ( connect to mysql )
        #products = product_form_bd()
        #product = products.connect_to_mysql()
        # close connect :)

        for pmname in self.paymethod:

            for x in range(0, self.ran):
            #add card
                try:
                    self.send_to_id(search, (random.choice(product)))
                    self.xpath(add_to_card)
                except UnexpectedAlertPresentException:
                    self.driver.switch_to_alert().accept()


                print("Add to card " + random.choice(product))

                # steps PM
            self.xpath(go_card)
            self.xpath(two_step_in_card)
            self.click_by_id(choose_default)
            self.xpath(go_pm_page)






            if pmname == "ideal":
                for pmideal in self.paymethod[pmname]:

                    self.send_to_id(search, (random.choice(product)))
                    self.xpath(add_to_card)

                    #steps PM
                    self.xpath(go_card)
                    self.xpath(two_step_in_card)
                    self.click_by_id(choose_default)
                    self.xpath(go_pm_page)

                    Select(self.driver.find_element(By.ID, "parentId-ideal")).select_by_value('{}'.format(pmideal))
                    self.xpath(buy_button)
                    self.driver.get("http://futurumshop.nl")










            elif pmname == 'ogonestd':

                for pmogonestd in self.paymethod[pmname]:


                    Select(self.id("parentId-ideal")).select_by_value('{}'.format(pmogonestd))
                    self.xpath(buy_button)



            else:

                    self.xpath("//input[@id='{}']".format(pmname))

                    self.xpath(buy_button)



    def tearDown(self):
        self.driver.quit()
