from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import MySQLdb
import random


class test_order_nl(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.page = self.driver.get("http://futurumshop.nl")
        self.driver.set_window_size(2000, 2000)
        self.paymethod = {"ideal":["ABNANL2A",  "RABONL2U", "INGBNL2A", "KNABNL2H", "SNSBNL2A", "RBRBNL21", "ASNBNL21", "TRIONL2U", "FVLBNL22"], "paypal": 'paypal',  "ogonestd":["visa", "aexpress", "mastercard"],"overboeking": 'overboeking', "rmbrs": 'rmbs', "mistercash": 'mistercash'}
        self.ran = random.randrange(2, 5)

    def test_ordernl(self):

        # add products
        product = []
        db = MySQLdb.connect(host='localhost', user='root', passwd='admiralxoxol', db='futurum')
        cur = db.cursor()
        cur.execute("select prodlevid from product where own_stock = '5' LIMIT 0, 20;")

        for base in cur.fetchall():
           product.append(base[0])


        #loggin futurumshop123@gmail,com

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
                    print(pmideal)
                    Select(self.driver.find_element(By.ID, "parentId-ideal")).select_by_value('{}'.format(pmideal))
                    self.driver.find_element(By.XPATH, "(//button[@class='btncta icon buy large orderButton nextstep checkout'])[1]")


        else:
            print(pmname)


    def tearDown(self):
        self.driver.quit()
