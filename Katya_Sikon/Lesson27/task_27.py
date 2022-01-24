import mysql.connector as mysql

db = mysql.connect(
    host="localhost",
    user="root",
    passwd="dr6210TY",
    database="test_db"
)

cursor = db.cursor()

# создание таблицы orders
cursor.execute("CREATE TABLE orders (ord_no INT(10), purch_amt FLOAT, ord_date DATE, customer_id INT(10), salesman_id INT(10))")

#вставка данных в таблицу
query = "INSERT INTO orders (ord_no, purch_amt, ord_date, customer_id, salesman_id) VALUES (%s, %s, %s, %s, %s)"
values = [
    (70001, 150.5, '2012-10-05', 3005, 5002),
    (70009, 270.65, '2012-09-10', 3001, 5005),
    (70002, 65.26, '2012-10-05', 3002, 5001),
    (70004, 110.5, '2012-08-17', 3009, 5003),
    (70007, 948.5, '2012-09-10', 3005, 5002),
    (70005, 2400.6, '2012-07-27', 3007, 5001),
    (70008, 5760, '2012-09-10', 3002, 5001),
    (70010, 1983.43, '2012-10-10', 3004, 5006),
    (70003, 2480.4, '2012-10-10', 3009, 5003),
    (70012, 250.45, '2012-06-27', 3008, 5002),
    (70011, 75.29, '2012-08-17', 3003, 5007),
    (70013, 3045.6, '2012-04-25', 3002, 5001)
]

cursor.executemany(query, values)
db.commit()
print(cursor.rowcount, "records inserted")

# Напечатайте номер заказа, дату заказа и количество для каждого заказа, Который продал продавец под номером: 5002
print('\n Номер заказа, дата заказа, количество для каждого заказа, который продал продавец под номером 5002')
cursor.execute("SELECT ord_no, ord_date, purch_amt FROM orders WHERE salesman_id = 5002")
print(cursor.fetchall())

# Напечатайте уникальные id продавца(salesman_id). Используйте distinct
print('\n Уникальные id продавцов')
cursor.execute("SELECT DISTINCT salesman_id FROM orders")
print(cursor.fetchall())

# Напечатайте по порядку данные о дате заказа, id продавца, номер заказа, количество
print('\nЗаказы по дате заказа')
cursor.execute("SELECT * FROM orders ORDER BY ord_date")
print(cursor.fetchall())

print('\nЗаказы по id продавца')
cursor.execute("SELECT * FROM orders ORDER BY salesman_id")
print(cursor.fetchall())

print('\nЗаказы по номеру заказа')
cursor.execute("SELECT * FROM orders ORDER BY ord_no")
print(cursor.fetchall())

print('\nЗаказы по количеству')
cursor.execute("SELECT * FROM orders ORDER BY purch_amt")
print(cursor.fetchall())

# Напечатайте заказы между 70001 и 70007(используйте between, and)
print('\nЗаказы между 70001 и 70007')
cursor.execute("SELECT * FROM orders WHERE ord_no BETWEEN 70001 AND 70007 ORDER BY ord_no")
print(cursor.fetchall())
