import mysql.connector
from mysql.connector import Error

# Database connection
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
            description VARCHAR(255) NOT NULL,
            amount DECIMAL(10, 2) NOT NULL,
            date DATE NOT NULL
        )
        ''')
        print("Connected to MySQL and ensured the database is ready.")

except Error as e:
    print(f"Error while connecting to MySQL: {e}")
    exit()

def add_expense(description, amount, date):
    try:
        cursor.execute(
            "INSERT INTO expenses (description, amount, date) VALUES (%s, %s, %s)",
            (description, amount, date)
        )
        connection.commit()
        print("Expense added successfully!")
    except Error as e:
        print(f"Failed to add expense: {e}")

def view_expenses():
    try:
        cursor.execute("SELECT * FROM expenses")
        rows = cursor.fetchall()

        if rows:
            print("\nExpenses:")
            print(f"{'ID':<5}{'Description':<30}{'Amount':<10}{'Date':<12}")
            print("-" * 60)
            for row in rows:
                print(f"{row[0]:<5}{row[1]:<30}{row[2]:<10}{row[3]:<12}")
        else:
            print("\nNo expenses found.")
    except Error as e:
        print(f"Failed to retrieve expenses: {e}")

def delete_expense(expense_id):
    try:
        cursor.execute("DELETE FROM expenses WHERE id = %s", (expense_id,))
        connection.commit()

        if cursor.rowcount > 0:
            print("Expense deleted successfully!")
        else:
            print("Expense not found.")
    except Error as e:
        print(f"Failed to delete expense: {e}")


def main():
    while True:
        print("\nExpense Manager")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter description: ")
            amount = input("Enter amount: ")
            date = input("Enter date (YYYY-MM-DD): ")
            add_expense(description, amount, date)

        elif choice == '2':
            view_expenses()

        elif choice == '3':
            expense_id = input("Enter the ID of the expense to delete: ")
            delete_expense(expense_id)

        elif choice == '4':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


if connection.is_connected():
    cursor.close()
    connection.close()
