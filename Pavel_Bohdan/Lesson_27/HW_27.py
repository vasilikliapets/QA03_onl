import mysql.connector as mysql

db = mysql.connect(host="localhost",
                   user="root",
                   passwd="********",
                   database="test_db"
                   )

cursor = db.cursor()

'''Заполнить таблицу данными, минимум 10 записей'''
# cursor.execute(
#     "CREATE TABLE orders (purch_amt FLOAT, ord_date VARCHAR(255), customer_id INT, salesman_id INT)")
# cursor.execute(
#     "ALTER TABLE orders ADD COLUMN ord_no INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST")
# query = "INSERT INTO orders (purch_amt, ord_date, customer_id, salesman_id) VALUES (%s, %s, %s, %s)"
# values = [
#     (150.5, "2012-10-05", 5, 2),
#     (270.65, "2012-09-10", 1, 5),
#     (65.26, "2012-10-05", 2, 1),
#     (110.5, "2012-08-17", 9, 3),
#     (948.5, "2012-09-10", 5, 2),
#     (2400.6, "2012-07-27", 7, 1),
#     (5760, "2012-09-10", 2, 1),
#     (1983.43, "2012-10-10", 4, 6),
#     (2480.4, "2012-10-10", 9, 3),
#     (250.45, "2012-06-27", 8, 2)
# ]

# cursor.executemany(query, values)
# db.commit()

'''1)	Напечатайте номер заказа, дату заказа и количество для каждого заказа, Который продал продавец под номером: 2
'''
# query = "SELECT * FROM orders WHERE salesman_id=2"
# cursor.execute(query)
'''2)	Напечатайте уникальные id продавца(salesman_id). Используйте distinct
'''
# query = "SELECT DISTINCT salesman_id from orders"
# cursor.execute(query)
'''3)	Напечатайте по порядку данные о дате заказа, id продавца, номер заказа, количество
'''
# query = "SELECT ord_date FROM orders ORDER BY ord_date"
# cursor.execute(query)
# query = "SELECT salesman_id FROM orders ORDER BY salesman_id"
# cursor.execute(query)
# query = "SELECT ord_no FROM orders ORDER BY ord_no"
# cursor.execute(query)
# query = "SELECT purch_amt FROM orders ORDER BY purch_amt"
# cursor.execute(query)
'''4)	Напечатайте заказы между 70001 и 70007(используйте between, and)
'''
# query = "SELECT * FROM orders WHERE ord_no BETWEEN 1 and 7"
# cursor.execute(query)
