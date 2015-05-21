from selenium import webdriver



class start_webdriver():

    def start_and_login(self):
        self.driver = webdriver.Chrome()
        self.page = self.driver.get("http://futurumshop.nl")
        self.driver.set_window_size(2000, 2000)

        return self.driver
