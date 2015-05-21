from startwork import start_webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import random
from  connect_to_bd import product_form_bd





class test_order_nl(unittest.TestCase):

    def setUp(self):

        # prepare browsing and webdriver for work
        start = start_webdriver()
        self.driver = start.start_and_login()
        # done

        self.paymethod = {"ideal":["ABNANL2A",  "RABONL2U", "INGBNL2A", "KNABNL2H", "SNSBNL2A", "RBRBNL21", "ASNBNL21", "TRIONL2U", "FVLBNL22"], "paypal": 'paypal',
                          "ogonestd":["visa", "aexpress", "mastercard"],"overboeking": 'overboeking', "rmbrs": 'rmbs', "mistercash": 'mistercash'}

        self.ran = random.randrange(2, 6)




    def test_ordernl(self):

        # add products ( connect to mysql )
        products = product_form_bd()
        product = products.connect_to_mysql()
        # close connect :)




        inlog = self.driver.find_element(By.XPATH, "//a[contains(text(), 'Inloggen')]")
        inlog.click()
        logname = self.driver.find_element(By.ID, "regid")
        logname.send_keys("futurumshop123@gmail.com")
        password = self.driver.find_element(By.ID, "password")
        password.send_keys("qwe123", Keys.ENTER)

        #add to card



        #pm
        for pmname in self.paymethod:

            if pmname == "ideal":
                for pmideal in self.paymethod[pmname]:

                    for x in range(1, self.ran):

                        search =  self.driver.find_element_by_id("fc_search").send_keys(random.choice(product), Keys.ENTER)
                        add_tocard = self.driver.find_element_by_xpath("(//div[@id='selectedProduct']//div/button)[2]").click()
                        print("Add to card " + random.choice(product))

        # steps to PM
                    click_card = self.driver.find_element(By.XPATH, "//div[@class='cartHeader']//a")
                    click_card.click()
                    step1 = self.driver.find_element(By.XPATH, "(//button[@class='btncta icon buy large checkout'])[1]")
                    step1.click()
                    step2 = self.driver.find_element(By.ID, "default")
                    step2.click()
                    go_pm = self.driver.find_element(By.XPATH, "(//form[@id='orderForm']//button)[1]")
                    go_pm.click()
        # PM

                    Select(self.driver.find_element(By.ID, "parentId-ideal")).select_by_value('{}'.format(pmideal))
                    buy = self.driver.find_element(By.XPATH, "(//button[@class='btncta icon buy large orderButton nextstep checkout'])[1]")
                    buy.click()

                    try:
                        self.driver.get("http://futurumshop.nl")
                        alarm = self.driver.switch_to_alert()
                        alarm.accept()
                    except NoSuchElementException, e: return False




            elif pmname == 'ogonestd':
                for pmogonestd in self.paymethod[pmname]:

                    for x in range(1, self.ran):

                        search =  self.driver.find_element_by_id("fc_search").send_keys(random.choice(product), Keys.ENTER)
                        add_tocard = self.driver.find_element_by_xpath("(//div[@id='selectedProduct']//div/button)[2]").click()
                        print("Add to card " + random.choice(product))

        # steps to PM
                    click_card = self.driver.find_element(By.XPATH, "//div[@class='cartHeader']//a")
                    click_card.click()
                    step1 = self.driver.find_element(By.XPATH, "(//button[@class='btncta icon buy large checkout'])[1]")
                    step1.click()
                    step2 = self.driver.find_element(By.ID, "default")
                    step2.click()
                    go_pm = self.driver.find_element(By.XPATH, "(//form[@id='orderForm']//button)[1]")
                    go_pm.click()
        # PM

                    Select(self.driver.find_element(By.ID, "parentId-ideal")).select_by_value('{}'.format(pmogonestd))
                    buy = self.driver.find_element(By.XPATH, "(//button[@class='btncta icon buy large orderButton nextstep checkout'])[1]")
                    buy.click()


            else:
                    for x in range(1, self.ran):

                        search =  self.driver.find_element_by_id("fc_search").send_keys(random.choice(product), Keys.ENTER)
                        add_tocard = self.driver.find_element_by_xpath("(//div[@id='selectedProduct']//div/button)[2]").click()
                        print("Add to card " + random.choice(product))

                    # steps to PM
                    click_card = self.driver.find_element(By.XPATH, "//div[@class='cartHeader']//a")
                    click_card.click()
                    step1 = self.driver.find_element(By.XPATH, "(//button[@class='btncta icon buy large checkout'])[1]")
                    step1.click()
                    step2 = self.driver.find_element(By.ID, "default")
                    step2.click()
                    go_pm = self.driver.find_element(By.XPATH, "(//form[@id='orderForm']//button)[1]")
                    go_pm.click()


                    other = self.driver.find_element(By.XPATH, "//input[@id='{}']".format(pmname))
                    other.click()

                    buy = self.driver.find_element(By.XPATH, "(//button[@class='btncta icon buy large orderButton nextstep checkout'])[1]")
                    buy.click()
                    self.driver.get("http://futurumshop.nl")

    def tearDown(self):
        self.driver.quit()
