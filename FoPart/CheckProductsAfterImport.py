from StartWork import *

class testProductAfterImpoert(StartWork):
    def setUp(self):
        self.OpenBrowser()

        self.fileproduct = open('prodlevid.txt', 'r')
        self.produtsid = []
        for id in self.fileproduct:
            self.produtsid.append(id.replace('\n', ''))

        self.fileproduct.close()

    def testRedirectproducts(self):

        for productid in self.produtsid:

            self.send_keys_id(self.cfg['button']['search'], productid)
            self.driver.implicitly_wait(3)
            if len(self.driver.find_elements(By.XPATH, "//ul[@class='col-xs-12']/li")) == 2:
                print("{} -> None visible".format(productid))
            elif len(self.driver.find_elements(By.XPATH, "//ul[@class='col-xs-12']/li")) == 0:
                print ("{} -> Home page".format(productid))

            self.clear('fc_search')

    def tearDown(self):
        self.driver.quit()
