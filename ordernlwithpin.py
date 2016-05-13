from startwork import *
from  Button_from_fo import *
import random





class test_ordernlwithpin(unittest.TestCase, start_webdriver):

    def setUp(self):

        self.start_and_login()
        self.paymethodnl = {"ideal":[ "ABNANL2A",  "RABONL2U", "INGBNL2A", "KNABNL2H", "SNSBNL2A", "RBRBNL21", "ASNBNL21", "TRIONL2U"],
                         "ogonestd":["visa", "aexpress", "mastercard"],"pin": 'pin', "mistercash":'mistercash'} #"paypal": 'paypal',
        self.deliverymethod ={"internamsterdam": 'internamsterdam', "internapeldoorn": 'internapeldoorn'}
        self.ran = random.randrange(2, 3)


    def test_ordernl(self):

        for method in self.deliverymethod:
            for pmname in self.paymethodnl:

                for x in range(0, self.ran):
            #add card

                    time.sleep(2)
                    self.send_keys_id(search, (random.choice(self.product)))
                    time.sleep(2)
                    self.click_by_xpath(add_to_card)

                self.click_by_xpath(go_card)
                time.sleep(2)
                self.click_by_xpath(two_step_in_card)
                time.sleep(2)
                self.click_by_id(self.deliverymethod[method])
                time.sleep(2)
                self.click_by_xpath(go_pm_page)



                if pmname == "ideal":
                    for pmideal in self.paymethodnl[pmname]:
                        self.driver.get(urlNL)
                        time.sleep(2)
                        self.send_keys_id(search, (random.choice(self.product)))
                        time.sleep(2)
                        self.click_by_xpath(add_to_card)
                        time.sleep(2)
                        self.click_by_xpath(go_card)
                        time.sleep(2)
                        self.click_by_xpath(two_step_in_card)
                        time.sleep(2)
                        self.click_by_id(self.deliverymethod[method])
                        time.sleep(2)
                        self.click_by_xpath(go_pm_page)
                        time.sleep(2)
                        idealss = self.driver.find_element(By.XPATH, "//select[@id='parentId-ideal']")
                        Select(idealss).select_by_value('{}'.format(pmideal))
                        time.sleep(2)
                        self.click_by_xpath(buy_button)
                        time.sleep(2)
                        self.click_by_xpath("//button[@class='btncta icon buy large checkout pull-right']")
                        time.sleep(2)
                        self.driver.get(urlNL)



                elif pmname == 'ogonestd':

                    for pmogonestd in self.paymethodnl[pmname]:
                        self.driver.get(urlNL)
                        time.sleep(2)
                        self.send_keys_id(search, (random.choice(self.product)))
                        time.sleep(2)
                        self.click_by_xpath(add_to_card)
                        time.sleep(2)
                        self.click_by_xpath(go_card)
                        time.sleep(2)
                        self.click_by_xpath(two_step_in_card)
                        time.sleep(2)
                        self.click_by_id(self.deliverymethod[method])
                        time.sleep(2)
                        self.click_by_xpath(go_pm_page)
                        time.sleep(2)
                        self.click_by_id('ogonestd')
                        time.sleep(2)
                        ogone = self.driver.find_element(By.XPATH, "//select[@id='parentId-ogonestd']")
                        Select(ogone).select_by_value('{}'.format(pmogonestd))
                        time.sleep(2)
                        self.click_by_xpath(buy_button)
                        time.sleep(2)
                        self.click_by_xpath("//button[@class='btncta icon buy large checkout pull-right']")
                        time.sleep(2)
                        self.driver.get(urlNL)


                else:
                    time.sleep(2)
                    print (pmname)
                    self.click_by_xpath("//input[@id='{}']".format(pmname))
                    time.sleep(2)
                    self.click_by_xpath(buy_button)
                    time.sleep(2)
                    self.click_by_xpath("//button[@class='btncta icon buy large checkout pull-right']")
                    time.sleep(2)
                    self.driver.get(urlNL)


    def tearDown(self):
        self.driver.quit()




