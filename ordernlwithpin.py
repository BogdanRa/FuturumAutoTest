from startwork import *

import random


class test_ordernlwithpin(start_webdriver):
    def setUp(self):

        self.StartAndLogin()
        self.paymethodnl = {
            "ideal": ["ABNANL2A", "RABONL2U", "INGBNL2A", "KNABNL2H", "SNSBNL2A", "RBRBNL21", "ASNBNL21", "TRIONL2U"],
            "ogonestd": ["visa", "aexpress", "mastercard"], "pin": 'pin',
            "mistercash": 'mistercash'}  # "paypal": 'paypal',

        self.deliverymethod = {"internamsterdam": 'internamsterdam', "internapeldoorn": 'internapeldoorn'}

    def test_ordernl(self):

        for method in self.deliverymethod:
            for pmname in self.paymethodnl:

                self.generatecart()
                self.PINdelivery(self.deliverymethod[method])

                if pmname == "ideal":
                    for pmideal in self.paymethodnl[pmname]:
                        self.driver.get(self.cfg['testenvr']['LiveNL'])
                        self.generatecart()
                        self.PINdelivery(self.deliverymethod[method])
                        time.sleep(2)
                        self.PMideal(pmideal)
                        self.placeorder()

                elif pmname == "ogonestd":

                    for pmogonestd in self.paymethodnl[pmname]:
                        self.driver.get(self.cfg['testenvr']['LiveNL'])
                        self.generatecart()
                        self.PINdelivery(self.deliverymethod[method])
                        time.sleep(2)
                        self.PMogone(pmogonestd)
                        self.placeorder()

                else:

                    self.click_by_xpath("//input[@id='{}']".format(pmname))
                    self.placeorder()

    def tearDown(self):
        self.driver.quit()
