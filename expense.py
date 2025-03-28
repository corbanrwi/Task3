import csv
import os

# Define the CSV file name
CSV_FILE = "expenses.csv"

# Ensure the file exists and has headers
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount"])

def add_expense():
    """Adds a new expense to the CSV file."""
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category (e.g., Food, Transport): ")
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
            print("-" * 30)
            for row in expenses:
                print(f"{row[0]} | {row[1]} | ${row[2]}")
            print("-" * 30)

    except FileNotFoundError:
        print("No expenses found. Add some first!")

def main():
    """Main menu for the expense tracker."""
    while True:
        print("\n📊 Expense Tracker")
        print("1️⃣ Add Expense")
        print("2️⃣ View Expenses")
        print("3️⃣ Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
