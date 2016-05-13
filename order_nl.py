from startwork import *
from  Button_from_fo import *
import random





class test_order_nl(unittest.TestCase, start_webdriver):

    def setUp(self):

        self.StartAndLogin(urlNL)
        self.paymethodnl = {"ideal":[ "ABNANL2A",  "RABONL2U", "INGBNL2A", "KNABNL2H", "SNSBNL2A", "RBRBNL21", "ASNBNL21", "TRIONL2U"],
                         "ogonestd":["visa", "aexpress", "mastercard"],"overboeking": 'overboeking', "rmbrs": 'rmbs', "mistercash":'mistercash'} #"paypal": 'paypal',


       

    def test_ordernl(self):


        for pmname in self.paymethodnl:

            for totalproductincart in range(0, self.ran):

                self.generatecart() # Generate cart with products from first search page ( Default sorting )
            self.verificationsteps() # Choose delivery and payment method
            


            if pmname == "ideal":
                for pmideal in self.paymethodnl[pmname]:
                    self.driver.get(urlNL)

                    self.generatecart()
                    self.verificationsteps()
                    time.sleep(2)
                    #self.click_by_id('ideal')
                    idealss = self.driver.find_element(By.XPATH, "//select[@id='parentId-ideal']")
                    Select(idealss).select_by_value('{}'.format(pmideal))

                    self.placeorder() # Place order on FO



            elif pmname == 'ogonestd':

                for pmogonestd in self.paymethodnl[pmname]:
                    self.driver.get(urlNL)
                    self.generatecart()
                    self.verificationsteps()


                    self.click_by_id('ogonestd')
                    ogone = self.driver.find_element(By.XPATH, "//select[@id='parentId-ogonestd']")
                    Select(ogone).select_by_value('{}'.format(pmogonestd))

                    self.placeorder()


            else:

                    self.click_by_xpath("//input[@id='{}']".format(pmname))
                    self.placeorder()


    def tearDown(self):
        self.driver.quit()




