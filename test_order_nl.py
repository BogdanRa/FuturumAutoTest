import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import MySQLdb



class test_order_nl(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.page = self.driver.get("http://futurumshop.nl")
        self.driver.set_window_size(2000, 2000)



    def test_ordernl(self):

        product = []
        db = MySQLdb.connect(host='localhost', user='root', passwd='admiralxoxol', db='futurum')
        cur = db.cursor()
        cur.execute("select prodlevid from product where own_stock = '2' LIMIT 0, 10;")

        for base in cur.fetchall():
           product.append(base[0])






        inlog = self.driver.find_element(By.XPATH, "//a[contains(text(), 'Inloggen')]")
        inlog.click()
        logname = self.driver.find_element(By.ID, "regid")
        logname.send_keys("futurumshop123@gmail.com")
        password = self.driver.find_element(By.ID, "password")
        password.send_keys("qwe123", Keys.ENTER)


        search =  self.driver.find_element_by_id("fc_search").send_keys(random.choice(product), Keys.ENTER)

        print("Push " + random.choice(product) + " in search")



    def tearDown(self):
        self.driver.quit()