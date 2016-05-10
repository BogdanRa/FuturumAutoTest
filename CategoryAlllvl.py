from startwork import *
#!/usr/bin/env python

class CheckCategory(start_webdriver, unittest.TestCase):


    def setUp(self):
        self.openbrowser()


    def testLinkscategory(self):
        category = self.driver.find_elements(By.XPATH, "//li[@class='top_menu_element inactive']/*//a")
        categorys = []
        for categlinks in category:
            if categlinks.get_attribute('href') not in categorys:
                categorys.append(categlinks.get_attribute('href'))

        for url in categorys:
            self.driver.get(url)

            try:
                banner = self.driver.find_element(By.XPATH, "//div[@class='row row--small-gutter'][1]/div[1]")
                if banner.is_displayed():
                    print "-> ", url

            except NoSuchElementException:
                pass

    def tearDown(self):
       self.driver.quit()
