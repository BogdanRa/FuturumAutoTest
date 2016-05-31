from startwork import *


class newuser(start_webdriver):

    def newuser(self):
        self.send_keys_id('newemail', self.cfg['login']['user'])
        button = self.driver.find_element_by_xpath("(//button[@class='btncta buy icon pull-right'])[2]")
        button.click()

