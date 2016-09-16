import MySQLdb
#from Config.config import *

class product_form_bd():
    def connect_to_mysql(self):
        product = []
        db = MySQLdb.connect(host=db_host, user=db_username, passwd=db_password, db=db_database)
        cur = db.cursor()
        cur.execute("select prodlevid from product where own_stock = 3 LIMIT 0, 30;")

        for base in cur.fetchall():
            product.append(base[0])

        return product
