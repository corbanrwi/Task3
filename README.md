# 📝 Expense Tracker (CSV-Based)

## 📌 Objective  
Build a **CLI Expense Tracker** using Python and CSV files to record, manage, and summarize expenses.  

## 🔍 Research Topics  
Before starting, research the following:  
- **CSV Handling (`csv` module)** – Reading, writing, and updating CSV files.  
- **Python Data Structures (`list`, `dict`)** – Organizing expense records.  
- **User Input Handling (`input()`)** – Taking user input for expenses.  
- **Basic File Handling (`open()`)** – Managing file reading and writing.  

## 🛠️ Features to Implement  
### ✅ 1. Add an Expense  
- Ask the user for:  
  - **Date** (YYYY-MM-DD)  
  - **Category** (e.g., Food, Transport, Shopping)  
  - **Amount** (e.g., 12.50)  
- Save this data in `expenses.csv` in the following format:  
  ```csv
  Date,Category,Amount
  2025-03-28,Food,12.50
  2025-03-28,Transport,8.00
  ```  

### ✅ 2. View All Expenses  
- Read the CSV file and **display all expenses** in a table format.

### ✅ 3. Delete an Expense  
- Allow the user to delete an expense by **date or category**.  

### ✅ 4. Show Total Expenses by Category  
- Summarize **total spending per category**.  

## 💡 Bonus Challenges  
💡 **Sort Expenses** – Sort by **date** or **amount**.  
💡 **Generate a Monthly Report** – Show total spending for each month.  
💡 **Graph Expenses (`matplotlib`)** – Visualize spending with a bar chart.  

## 🛠️ Starter Code  
Here’s a simple Python script to get you started:  

```python
import csv
import os

CSV_FILE = "expenses.csv"

if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount"])

def add_expense():
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category (e.g., Food, Transport): ")
    amount = input("Enter the amount spent: ")

    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])

    print("✅ Expense added successfully!\n")

def view_expenses():
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
```

---  

## 💙 Submission Guidelines  
- 📄 Submit your **Python script (`.py` file)**.  
- 📷 Include a **screenshot of your program running**.  
- 📝 Write a short **report** explaining how it works.  

Good luck! 🚀

