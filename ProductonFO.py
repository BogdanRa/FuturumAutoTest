from startwork import *
from config.config import *


class productscheck_test(unittest.TestCase, start_webdriver):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://testing.futurumshop.nl')
        self.driver.set_window_size(2000, 2000)
        self.fileproduct = open('prodlevid.txt', 'r')
        self.produtsid = []
        for id in self.fileproduct:
            self.produtsid.append(id)

        self.fileproduct.close()

    def testproducts(self):

        for prid in self.produtsid:
            self.send_keys_id(search, (prid))
            if len(self.driver.find_elements(By.XPATH, "//ul[@class='col-xs-12']/li")) == 2:
                print "{} None visible".format(prid)
            elif len(self.driver.find_elements(By.XPATH, "//ul[@class='col-xs-12']/li")) == 0:
                print "{} Home page".format(prid)
            time.sleep(1.3)
            self.clear('fc_search')

    def tearDown(self):
        self.driver.quit()
