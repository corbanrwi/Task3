import csv
import os
from collections import defaultdict

CSV_FILE = "expenses.csv"

# Ensure the file exists and has headers
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount"])

def add_expense():
    """Adds a new expense to the CSV file."""
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category (e.g., Food, Transport, Shopping): ")
    amount = input("Enter the amount spent: ")

    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])
    
    print("✅ Expense added successfully!\n")

def view_expenses():
    """Displays all recorded expenses."""
    try:
        with open(CSV_FILE, mode="r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            expenses = list(reader)

            if not expenses:
                print("No expenses recorded yet.")
                return

            print("\n📌 Your Expenses:")
            print("-" * 40)
            print("Date         | Category      | Amount ($)")
            print("-" * 40)
            for row in expenses:
                print(f"{row[0]:<12} | {row[1]:<12} | ${row[2]}")
            print("-" * 40)
    except FileNotFoundError:
        print("No expenses found. Add some first!")

def delete_expense():
    """Deletes an expense by date or category."""
    criteria = input("Delete by (date/category): ").strip().lower()
    value = input("Enter the value to delete: ").strip()
    
    with open(CSV_FILE, mode="r") as file:
        reader = csv.reader(file)
        rows = list(reader)
    
    header, expenses = rows[0], rows[1:]
    
    if criteria == "date":
        expenses = [row for row in expenses if row[0] != value]
    elif criteria == "category":
        expenses = [row for row in expenses if row[1].lower() != value.lower()]
    else:
        print("❌ Invalid choice.")
        return
    
    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(expenses)
    
    print("✅ Expense(s) deleted successfully!\n")

def total_expenses_by_category():
    """Shows total expenses per category."""
    totals = defaultdict(float)
    
    with open(CSV_FILE, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            totals[row[1]] += float(row[2])
    
    print("\n📊 Total Expenses by Category:")
    print("-" * 30)
    for category, total in totals.items():
        print(f"{category}: ${total:.2f}")
    print("-" * 30)

def main():
    """Main menu for the expense tracker."""
    while True:
        print("\n📊 Expense Tracker")
        print("1️⃣ Add Expense")
        print("2️⃣ View Expenses")
        print("3️⃣ Delete Expense")
        print("4️⃣ Show Total Expenses by Category")
        print("5️⃣ Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            total_expenses_by_category()
        elif choice == "5":
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
