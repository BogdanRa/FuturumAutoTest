from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import unittest
import MySQLdb





class test_order_nl(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.page = self.driver.get("http://futurumshop.nl")
        self.driver.set_window_size(2000, 2000)
        product = []
        db = MySQLdb.connect(host='localhost', user='root', passwd='admiralxoxol', db='futurum')
        cur = db.cursor()
        cur.execute("select prodlevid from product where own_stock = '2' LIMIT 0, 20;")

        for base in cur.fetchall():
            product.append(base[0])


    def test_ordernl(self):

        inlog = self.driver.find_element(By.XPATH, "//a[contains(text(), 'Inloggen')]")
        inlog.click()
        logname = self.driver.find_element(By.ID, "regid")
        logname.send_keys("futurumshop123@gmail.com")
        password = self.driver.find_element(By.ID, "password")
        password.send_keys("qwe123")
        buttonlog = self.driver.find_element(By.XPATH, "//p/button[@class='btncta']")
        buttonlog.click()



    def tearDown(self):
        self.driver.quit()