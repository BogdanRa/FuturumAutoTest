from selenium import webdriver
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
        self.paymethod = ["ideal", "paypal", "ogonestd", "overboeking", "rmbrs", "mistercash"]


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

        ran = random.randrange(2, 13)
        for x in range(1, ran):
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

        #pm
        for pmname in self.paymethod:
            pm = self.driver.find_element(By.ID, '{0!s}'.format(pmname))
            if pmname == "ideal":
               ideal = self.driver.find_elements(By.XPATH, "//select[@id='parentId-ideal']/option[position()>1]")
               for i in ideal:
                   print(i.get_attribute('value'))
                #Select(self.driver.find_element(By.ID, "parentId-ideal")).select_by_value("INGBNL2A")

    def tearDown(self):
        self.driver.quit()