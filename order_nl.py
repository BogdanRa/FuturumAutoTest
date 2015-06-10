from startwork import start_webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import random
#from  connect_to_bd import product_form_bd
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.support import expected_conditions as EC



class test_order_nl(unittest.TestCase):

    def setUp(self):

        # prepare browsing and webdriver for work
        self.start = start_webdriver()
        self.driver = self.start.start_and_login()
        self.xpath = self.start.find_by_xpath
        self.id = self.start.find_by_id
        self.send_to_id = self.start.send_keys_id
        self.send_to_xpath = self.start.send_keys_xpath

        # done

        self.paymethod = {"ideal":[ "ASNBNL21", "TRIONL2U", "FVLBNL22"], "paypal": 'paypal'}
                          #"ogonestd":["visa", "aexpress", "mastercard"],"overboeking": 'overboeking', "rmbrs": 'rmbs', "mistercash": 'mistercash'}
                           # "ABNANL2A",  "RABONL2U", "INGBNL2A", "KNABNL2H", "SNSBNL2A", "RBRBNL21",
        self.ran = random.randrange(2, 10)




    def test_ordernl(self):


        product = ["6003-0072-N1011", "6003-0136-N1202", "6004-0209-001-N1102",
                   "6004-0209-002-N1102","6004-0293-001-N1108", "6004-0293-004-N1108", "6004-0294-003-N1108", "6004-0294-004-N1108",
                   "6004-0296-N1108", "6004-0298-N1108", "6004-0300-N1108", "6004-0307-005-N1108", "6004-0385-N1208",
                    "6004-0410-003-N1302", "6004-0410-004-N1302", "6004-0411-003-N1302", "6004-0431-001-N1302", "6004-0442-N1303",
                   "6004-0459-N1304", "6004-0470-002-N1307", "6004-0470-004-N1307", "6004-0514-002-N1308", "6004-0519-004-N1308",
                    "6004-0520-004-N1308", "6004-0577-001-N1502", "6004-0580-002-N1502", "6004-0591-003-N1502", "6004-0593-004-N1502"]
        # add products ( connect to mysql )
        #products = product_form_bd()
        #product = products.connect_to_mysql()
        # close connect :)

        for pmname in self.paymethod:

            for x in range(0, self.ran):
                        #add card
                        self.send_to_id("fc_search", (random.choice(product)))
                        self.xpath("(//div[@id='selectedProduct']//div/button)[2]")
                        print("Add to card " + random.choice(product))

            #steps PM
            self.xpath("//div[@class='cartHeader']//a")
            self.xpath("(//button[@class='btncta icon buy large checkout'])[1]")
            self.id("default")
            self.xpath("(//form[@id='orderForm']//button)[1]")




            if pmname == "ideal":
                for pmideal in self.paymethod[pmname]:
                    #add card
                    self.send_to_id("fc_search", (random.choice(product)))
                    self.xpath("(//div[@id='selectedProduct']//div/button)[2]")
                    print("Add to card " + random.choice(product))

                    #steps PM
                    self.xpath("//div[@class='cartHeader']//a")
                    self.xpath("(//button[@class='btncta icon buy large checkout'])[1]")
                    self.id("default")
                    self.xpath("(//form[@id='orderForm']//button)[1]")
                    Select(self.driver.find_element(By.ID, "parentId-ideal")).select_by_value('{}'.format(pmideal))
                    self.xpath("(//button[@class='btncta icon buy large orderButton nextstep checkout'])[1]")

                    #self.driver.get("http://futurumshop.nl")
                    try:
                        self.driver.get("http://futurumshop.nl")

                    except NoSuchElementException, e:
                        alarm = self.driver.switch_to_alert()
                        alarm.accept()



            elif pmname == 'ogonestd':

                for pmogonestd in self.paymethod[pmname]:


                    Select(self.id("parentId-ideal")).select_by_value('{}'.format(pmogonestd))
                    self.xpath("(//button[@class='btncta icon buy large orderButton nextstep checkout'])[1]")



            else:

                    self.xpath("//input[@id='{}']".format(pmname))

                    self.xpath("(//button[@class='btncta icon buy large orderButton nextstep checkout'])[1]")
                    self.driver.get("http://futurumshop.nl")


    def tearDown(self):
        self.driver.quit()
