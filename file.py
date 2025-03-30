import os

# File to store expenses
FILE_NAME = "expenses.txt"

def add_expense():
    """Add an expense to the file."""
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category (e.g., Food, Transport, etc.): ")
    amount = input("Enter the amount: ")

    # Save to file
    with open(FILE_NAME, "a") as file:
        file.write(f"{date},{category},{amount}\n")
    print("Expense added successfully!")

def view_expenses():
    """View all expenses."""
    if not os.path.exists(FILE_NAME):
        print("No expenses recorded yet!")
        return
    
    with open(FILE_NAME, "r") as file:
        print("\nDate       | Category       | Amount")
        print("-------------------------------------")
        for line in file:
            date, category, amount = line.strip().split(",")
            print(f"{date:10} | {category:14} | {amount}")
    print("-------------------------------------")

def search_by_date():
    """Search for expenses on a specific date."""
    date_to_search = input("Enter the date to search (YYYY-MM-DD): ")
    
    found = False
    with open(FILE_NAME, "r") as file:
        print("\nDate       | Category       | Amount")
        print("-------------------------------------")
        for line in file:
            date, category, amount = line.strip().split(",")
            if date == date_to_search:
                print(f"{date:10} | {category:14} | {amount}")
                found = True
        if not found:
            print("No expenses found for the given date.")
    print("-------------------------------------")

def summarize_expenses():
    """Summarize total expenses and category-wise breakdown."""
    if not os.path.exists(FILE_NAME):
        print("No expenses recorded yet!")
        return
    
    total = 0
    category_totals = {}
    
    with open(FILE_NAME, "r") as file:
        for line in file:
            _, category, amount = line.strip().split(",")
            amount = float(amount)
            total += amount
            category_totals[category] = category_totals.get(category, 0) + amount
    
    print(f"\nTotal Expenses: {total:.2f}")
    print("\nCategory-wise Breakdown:")
    for category, amount in category_totals.items():
        print(f"  {category}: {amount:.2f}")

def main():
    """Main program loop."""
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search by Date")
        print("4. Summarize Expenses")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            search_by_date()
        elif choice == "4":
            summarize_expenses()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
