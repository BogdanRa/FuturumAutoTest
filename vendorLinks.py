from startwork import *


class vendorLinks(start_webdriver):


    def setUp(self):
        self.openbrowser()


    def testvendorLinks(self):

            self.vendorFooter = []
            top = self.driver.find_elements_by_xpath("//div[@class='hidden-xs hidden-sm row vendors inverted']/ul/li/a")
            for links in top:
                self.vendorFooter.append((str((links.get_attribute('href')))))

            for vendrolinks in range(0, len(self.vendorFooter)):
                self.driver.get(self.vendorFooter[vendrolinks])

                if self.driver.title in 'Futurumshop | Specialist in Fietsen,Hardlopen,Buitensport':
                    print self.vendorFooter[vendrolinks],'empty url'



    def tearDown(self):
        self.driver.quit()
