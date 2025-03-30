import os


# File to store expenses


FILE_NAME = "expenses.txt"

def add_expense():
    """Add an expense to the file."""
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category (e.g., Food, Transport, etc.): ")
    try:
        amount = float(input("Enter the amount: "))
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return

    # Save to file
    with open(FILE_NAME, "a") as file:
        file.write(f"{date},{category},{amount}\n")
    print("Expense added successfully!\n")

def view_expenses():
    """View all expenses."""
    if not os.path.exists(FILE_NAME):
        print("No expenses recorded yet!\n")
        return

    with open(FILE_NAME, "r") as file:
        print("\nDate       | Category       | Amount")
        print("-------------------------------------")
        for line in file:
            date, category, amount = line.strip().split(",")
            print(f"{date:10} | {category:14} | {amount}")
    print("-------------------------------------\n")

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
    print("-------------------------------------\n")

def summarize_expenses():
    """Summarize total expenses and category-wise breakdown."""
    if not os.path.exists(FILE_NAME):
        print("No expenses recorded yet!\n")
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

    print()

def export_expenses_to_csv():
    """Export expenses to a CSV file."""
    import csv

    output_file = "expenses_export.csv"

    if not os.path.exists(FILE_NAME):
        print("No expenses to export!\n")
        return

    with open(FILE_NAME, "r") as file:
        with open(output_file, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Date", "Category", "Amount"])
            for line in file:
                writer.writerow(line.strip().split(","))

    print(f"Expenses successfully exported to {output_file}!\n")

def main():
    """Main program loop."""
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search by Date")
        print("4. Summarize Expenses")
        print("5. Export Expenses to CSV")
        print("6. Exit")

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
            export_expenses_to_csv()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
