import MySQLdb


class product_form_bd():

    def connect_to_mysql(self):

        product = []
        db = MySQLdb.connect(host='localhost', user='root', passwd='admiralxoxol', db='futurum')
        cur = db.cursor()
        cur.execute("select prodlevid from product where own_stock = 3 LIMIT 0, 30;")

        for base in cur.fetchall():
           product.append(base[0])

        return product