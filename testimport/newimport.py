#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import *
from faker import Faker

'''
Creating import file with 7 important columns (vendorID, productID, vendorName,  productName, adviesprijs, verkoopprijs, product stock) 
for a little import's test. 
'''

#make massive with vendor name	
#make a product name
Namegenerator = Faker()

#count = raw_input("How many products are you need?: ")
#product stock
productstock = ['2-6 werkdagen', 'ja, op voorraad', 'Onbekende levertijd', 'week 1',
				'week 10', 'week 11', 'week 12', 'week 13']

#creating import file with 7 columns (vendorID, productID, vendorName,  productName, adviesprijs, verkoopprijs, product stock)
imports = open ('/home/bohdan/importfile/import.txt', 'w')
vendors ={
"NewVendor1": 1000,
"NewVendor2": 2000,
"NewVendor3": 3000,
"NewVendor4": 4000,
"Newvendor5": 5000}





for i in vendors:
	for count in range(10):
	

		partproductid2 = randint(1000, 9999)
	for z in range(1, 9):		
		partproductid3 = z
		partproductid4 = randint(1000, 9999)
		#vendorsecondint = randint(1000, 9999)
		adviesprijs = randint(10, 200)
		verkoopprijs = adviesprijs + 20
 		imports.write("{}-{}-00{}-N{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(
 							vendors[i], partproductid2, partproductid3, partproductid4, i, 
 							Namegenerator.company(), Namegenerator.username(), adviesprijs, verkoopprijs, choice(productstock))),
	 
print "File was created successfuly with",count+1,"products"

imports.close()


