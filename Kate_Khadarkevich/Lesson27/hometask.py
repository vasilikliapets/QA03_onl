import mysql.connector as mysql

db = mysql.connect(host="localhost",
                   user="root",
                   passwd="0103Byn20",
                   database='test_db')

cursor = db.cursor()

#cursor.execute(
#    "CREATE TABLE orders (ord_no INT, purch_amt FLOAT, ord_date DATE, customer_id INT, salesman_id INT)")

#query = "INSERT INTO orders (ord_no, purch_amt, ord_date, customer_id, salesman_id) VALUES (%s, %s, %s, %s, %s)"
#values = [
#    (70001, 150.5, "2012-10-05", 3005, 5002),
#    (70009, 270.65, "2012-09-10", 3001, 5005),
#    (70002, 65.26, "2012-10-05", 3002, 5001),
#    (70004, 110.5, "2012-08-17", 3009, 5003),
#    (70007, 948.5, "2012-09-10", 3005, 5002),
#    (70005, 2400.6, "2012-07-27", 3007, 5001),
#    (70008, 5760, "2012-09-10", 3002, 5001),
#    (70010, 1983.43, "2012-10-10", 3004, 5006),
#    (70003, 2480.4, "2012-10-10", 3009, 5003),
#    (70012, 250.45, "2012-06-27", 3008, 5002)
#]
#cursor.executemany(query, values)
db.commit()
#print(cursor.rowcount, "records inserted")

# Напечатайте номер заказа, дату заказа и количество для каждого заказа, Который продал продавец под номером: 5002
cursor.execute("SELECT ord_no, purch_amt, ord_date  FROM orders WHERE salesman_id=5002")
print(cursor.fetchall())

# Напечатайте уникальные id продавца(salesman_id). Используйте distinct
cursor.execute("SELECT DISTINCT salesman_id from orders")
print(cursor.fetchall())

# Напечатайте по порядку данные о дате заказа, id продавца, номер заказа, количество
cursor.execute("SELECT ord_date FROM orders ORDER BY ord_date")
print(cursor.fetchall())
cursor.execute("SELECT salesman_id FROM orders ORDER BY salesman_id")
print(cursor.fetchall())
cursor.execute("SELECT ord_no FROM orders ORDER BY ord_no")
print(cursor.fetchall())
cursor.execute("SELECT purch_amt FROM orders ORDER BY purch_amt")
print(cursor.fetchall())


# Напечатайте заказы между 70001 и 70007(используйте between, and)
cursor.execute("SELECT * FROM orders WHERE ord_no BETWEEN 70001 AND 70007")
print(cursor.fetchall())

