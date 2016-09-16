from StartWork import *


class ProductsFO(StartWork):

    def setUp(self):
        self.OpenBrowser()
        self.fileproduct = open('prodlevid.txt', 'r')
        self.productsid = []
        for id in self.fileproduct:
            self.productsid.append(id)

        self.fileproduct.close()

    def testproducts(self):

        for prodcutid in self.productsid:
            self.send_keys_id(self.cfg['button']['search'], (prodcutid))
            if len(self.driver.find_elements(By.XPATH, "//ul[@class='col-xs-12']/li")) == 2:
                print("{} None visible".format(prodcutid))
            elif len(self.driver.find_elements(By.XPATH, "//ul[@class='col-xs-12']/li")) == 0:
                print("{} Home page".format(prodcutid))
            time.sleep(1.3)
            self.clear('fc_search')

    def tearDown(self):
        self.driver.quit()
