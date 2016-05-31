from startwork import *
from config.config import *

class testProductAfterImpoert(unittest.TestCase, start_webdriver):
    def setUp(self):
        self.openbrowser()
        self.fileproduct = open('prodlevid.txt', 'r')
        self.produtsid = []
        for id in self.fileproduct:
            self.produtsid.append(id.replace('\n', ''))

        self.fileproduct.close()

    def testRedirectproducts(self):

        for prid in self.produtsid:

            self.send_keys_id(search, prid)
            self.driver.implicitly_wait(3)
            if len(self.driver.find_elements(By.XPATH, "//ul[@class='col-xs-12']/li")) == 2:
                print "{} -> None visible".format(prid)
            elif len(self.driver.find_elements(By.XPATH, "//ul[@class='col-xs-12']/li")) == 0:
                print "{} -> Home page".format(prid)

            self.clear('fc_search')

    def tearDown(self):
        self.driver.quit()
