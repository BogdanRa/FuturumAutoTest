from random import *


vendors = open('/home/bohdan/new/testimport/vendorname', 'r')
vendorsname = []
for ven in vendors:
	vendorsname.append(ven.replace('\n', ''))
vendors.close()

product = open ('/home/bohdan/new/testimport/productsname', 'r')
productsname = []

for pr in product:
	
	productsname.append(pr.replace('\n', ''))
product.close()


stocks = open ('/home/bohdan/new/testimport/stock', 'r')
productstock = []

for prs in stocks:
	
	productstock.append(prs.replace('\n', ''))
stocks.close()




imports = open ('/home/bohdan/new/testimport/import.txt', 'w')
for count in range(1, 10):
		id1 = randint(1000, 9999)
		id2 = randint(1000, 9999)
		id3 = randint(1000, 9999)
		id4 = randint(1000, 9999)
		vendorsecondint = randint(1000, 9999)
		adviesprijs = randint(10, 200)
		verkoopprijs = adviesprijs + 20
 		imports.write("{}-{}-{}-N{}\t{}-{}\t{}\t{}\t{}\t{}\t{}\n".format(id1, id2, id3, id4, id1, vendorsecondint, choice(productsname), choice(vendorsname), adviesprijs, verkoopprijs, choice(productstock))),
imports.close()


