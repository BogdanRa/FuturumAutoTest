# coding=utf-8
#!/usr/bin/env python

from startwork import *
from Button_from_fo import *


class test_orderDE(unittest.TestCase, start_webdriver):
    def setUp(self):

        self.start_work_DE()
        self.paymethodde = ['visa', 'mastercard', 'aexpress'] #'paypal'
        self.ran = random.randrange(2, 4)

    def test_orderde(self):

        try:
            for pmname in self.paymethodde:

                for x in range(0, self.ran):
                    self.ranproduct = random.choice(self.product)
                    print self.ranproduct
                    time.sleep(2)
                    self.send_keys_id(search, (self.ranproduct))
                    time.sleep(2)
                    self.click_by_xpath(add_to_card)

                self.click_by_xpath(go_card)
                time.sleep(2)
                self.click_by_xpath(two_step_in_card)
                time.sleep(2)
                self.click_by_id(choose_default)
                time.sleep(2)
                self.click_by_xpath(go_pm_page)

                time.sleep(2)
                self.click_by_id('{}'.format(pmname))
                time.sleep(2)
                self.click_by_xpath(buy_button)
                time.sleep(2)
                self.click_by_id('agree')
                time.sleep(2)
                self.click_by_xpath("//button[@class='btncta icon buy large checkout pull-right']")
                time.sleep(2)
                self.driver.get(urlDE)

        except NoSuchElementException:
            print ("last element not found", self.ranproduct)



    def tearDown(self):
        self.driver.quit()
