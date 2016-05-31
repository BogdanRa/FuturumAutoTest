# coding=utf-8
#!/usr/bin/env python

from startwork import *
from Button_from_fo import *


class test_orderDE(start_webdriver):

    def setUp(self):
        self.StartAndLogin()



    def test_orderde(self):

        try:
            for pmname in self.cfg['PaymentmethodDE']:

                for totalproductincart in range(0, self.ran):
                    self.generatecart()
                self.verificationsteps()


                self.click_by_id('{}'.format(pmname))
                self.click_by_xpath(buy_button)
                self.click_by_id('agree')
                self.click_by_xpath("//button[@class='btncta icon buy large checkout pull-right']")
                time.sleep(1)
                self.driver.get(urlDE)

        except NoSuchElementException:
            print ("last element not found")



    def tearDown(self):
        self.driver.quit()



