from startwork import *
from  Button_from_fo import *
import random





class test_ordernlwithpin(unittest.TestCase, start_webdriver):

    def setUp(self):

        self.StartAndLogin()
        self.paymethodnl = {"ideal":[ "ABNANL2A",  "RABONL2U", "INGBNL2A", "KNABNL2H", "SNSBNL2A", "RBRBNL21", "ASNBNL21", "TRIONL2U"],
                         "ogonestd":["visa", "aexpress", "mastercard"],"pin": 'pin', "mistercash":'mistercash'} #"paypal": 'paypal',
        self.deliverymethod ={"internamsterdam": 'internamsterdam', "internapeldoorn": 'internapeldoorn'}
        self.ran = random.randrange(2, 3)


    def test_ordernl(self):

        for method in self.deliverymethod:
            for pmname in self.paymethodnl:

                for x in range(0, self.ran):


                    self.generatecart()

                self.PINdelivery(self.deliverymethod[method])



                if pmname == "ideal":
                    for pmideal in self.paymethodnl[pmname]:
                        self.driver.get(urlNL)
                        self.generatecart()
                        self.PINdelivery(self.deliverymethod[method])

                        idealss = self.driver.find_element(By.XPATH, "//select[@id='parentId-ideal']")
                        Select(idealss).select_by_value('{}'.format(pmideal))

                        self.placeorder()



                elif pmname == 'ogonestd':

                    for pmogonestd in self.paymethodnl[pmname]:
                        self.driver.get(urlNL)
                        self.generatecart()
                        self.PINdelivery(self.deliverymethod[method])

                        self.click_by_id('ogonestd')
                        time.sleep(2)
                        ogone = self.driver.find_element(By.XPATH, "//select[@id='parentId-ogonestd']")
                        Select(ogone).select_by_value('{}'.format(pmogonestd))

                        self.placeorder()


                else:

                        self.click_by_xpath("//input[@id='{}']".format(pmname))
                        self.placeorder()


    def tearDown(self):
        self.driver.quit()




