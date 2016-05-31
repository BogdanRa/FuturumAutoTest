# -*- coding: utf-8 -*-
# Database settings
import os

db_host = 'database-server'
db_username = 'futurum2'
db_password = 'futurum'
db_database = 'futurum'

# Shop settings
url = 'http://fo2.develop.nl'

# Search settings
urlNL = "http://fo2.develop.nl/zoeken/?sortBy[price]=asc&itemPerPage=50"
urlDE = "http://fo2.develop.de/suche/?q="

# Customer settings
customerLogin = 'alexey_trishin@bintime.com'
customerPassword = 'q1w2e3r4'

# NL
search = "fc_search"
add_to_card = "(//div[@id='selectedProduct']//button)[2]"
go_card = "//div[@class='cartHeader']//a"
two_step_in_card = "(//div[@id='content']//button)[1]"
go_pm_page = "(//div[@id='content']//button)[1]"
buy_button = "//span[@class='paymentOptions active']/button"

# Delivery method
choose_default = "default"
internamsterdam = "internamsterdam"
internapeldoorn = "internapeldoorn"

# DE

uberweisung = "(//input[@class='paymentmethod'])[2]"
paypal = 'paypal'
sofort = 'sofort'
visa = 'visa'
mastercard = 'mastercard'
aexpress = 'aexpress'
nachnahme = 'nachnahme'

agree = "//input[@id='agree']"

#testimport
#ymlfile = open(os.path.join("/home/bohdan/FuturumAutoTest/sandbox/yamltest.yml"), "r")
#importfilepath = '/home/bohdan/importfile/import.txt'
