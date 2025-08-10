import pandas as pd
from datetime import datetime
import os

FILENAME = "expenses.csv"

# Ensure CSV file exists
if not os.path.exists(FILENAME):
    pd.DataFrame(columns=["Date", "Category", "Amount", "Description"]).to_csv(FILENAME, index=False)

def add_expense():
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
    if date.strip() == "":
        date = datetime.today().strftime("%Y-%m-%d")
    category = input("Enter category (Food, Transport, Shopping, etc.): ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    df = pd.read_csv(FILENAME)
    new_entry = pd.DataFrame([[date, category, amount, description]],
                              columns=["Date", "Category", "Amount", "Description"])
    df = pd.concat([df, new_entry], ignore_index=True)
    df.to_csv(FILENAME, index=False)
    print("✅ Expense added successfully!\n")

def view_expenses():
    df = pd.read_csv(FILENAME)
    if df.empty:
        print("No expenses found.")
    else:
        print("\nAll Expenses:\n")
        print(df.to_string(index=False))
    print()

def category_summary():
    df = pd.read_csv(FILENAME)
    if df.empty:
        print("No data to summarize.")
    else:
        summary = df.groupby("Category")["Amount"].sum()
        print("\nTotal Expenses by Category:\n")
        print(summary)
    print()

def search_expense():
    keyword = input("Enter keyword to search in description: ").lower()
    df = pd.read_csv(FILENAME)
    results = df[df["Description"].str.lower().str.contains(keyword, na=False)]
    if results.empty:
        print("No matching expenses found.")
    else:
        print("\nSearch Results:\n")
        print(results.to_string(index=False))
    print()

def main():
    while True:
        print("===== Personal Expense Tracker =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Category Summary")
        print("4. Search Expenses")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            category_summary()
        elif choice == "4":
            search_expense()
        elif choice == "5":
            print("Goodbye! 💰")
            break
        else:
            print("Invalid choice, try again.\n")

if __name__ == "__main__":
    main()
