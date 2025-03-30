import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='password',
        database='expenses_db'
    )
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS expenses_db")
        cursor.execute("USE expenses_db")
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS expenses (
                id INT AUTO_INCREMENT PRIMARY KEY,
                description VARCHAR(255),
                amount DECIMAL(10, 2),
                date DATE
            )
        ''')
        print("Database and table setup successful.")
except Error as e:
    print(f"Error: {e}")
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
