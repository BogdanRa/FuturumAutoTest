from random import *
from faker import Faker
'''
Creating import file with 7 important columns (vendorID, productID, vendorName,  productName, adviesprijs, verkoopprijs, product stock) 
for a little import's test. 

p.s.
need some refactoring
'''

#make massive with a vendors name	
#make a product name
Namegenerator = Faker()


#product stock
productstock = ['2-6 werkdagen', 'ja, op voorraad', 'Onbekende levertijd', 'week 1',
				'week 10', 'week 11', 'week 12', 'week 13']

#creating import file with 7 columns (vendorID, productID, vendorName,  productName, adviesprijs, verkoopprijs, product stock)
imports = open ('/home/bohdan/importfile/import.txt', 'w') 
for count in range(1, 10):
		partproductid1 = randint(1000, 9999)
		partproductid2 = randint(1000, 9999)
		partproductid3 = randint(1000, 9999)
		partproductid4 = randint(1000, 9999)
		vendorsecondint = randint(1000, 9999)
		adviesprijs = randint(10, 200)
		verkoopprijs = adviesprijs + 20		
 		imports.write("{}-{}-{}-N{}\t{}-{}\t{}\t{}\t{}\t{}\t{}\n".format(partproductid1, partproductid2, partproductid3, partproductid4, partproductid1, 
 										vendorsecondint, Namegenerator.name(), Namegenerator.username(), adviesprijs, verkoopprijs, choice(productstock))),
print "File was created successfuly "
imports.close()


