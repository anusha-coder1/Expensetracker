import csv
import os

# File to store expenses
FILE_NAME = "expenses.csv"

def load_expenses():
    """Load existing expenses from a CSV file."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='r') as file:
            reader = csv.DictReader(file)
            return list(reader)
    else:
        return []

def save_expenses(expenses):
    """Save expenses to a CSV file."""
    with open(FILE_NAME, mode='w', newline='') as file:
        fieldnames = ["Date", "Category", "Description", "Amount"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expenses)

def add_expense(expenses):
    """Add a new expense."""
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g., Food, Transport, Bills): ")
    description = input("Enter description: ")
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Expense not added.")
        return expenses

    new_expense = {
        "Date": date,
        "Category": category,
        "Description": description,
        "Amount": f"{amount:.2f}"
    }

    expenses.append(new_expense)
    print("Expense added successfully.")
    return expenses

def view_expenses(expenses):
    """View all expenses."""
    if not expenses:
        print("No expenses recorded.")
    else:
        print(f"{'Date':<15}{'Category':<15}{'Description':<30}{'Amount':<10}")
        print("-" * 70)
        for expense in expenses:
            print(f"{expense['Date']:<15}{expense['Category']:<15}{expense['Description']:<30}{expense['Amount']:<10}")

def view_summary(expenses):
    """View a summary of expenses by category."""
    if not expenses:
        print("No expenses recorded.")
    else:
        summary = {}
        for expense in expenses:
            category = expense['Category']
            amount = float(expense['Amount'])
            summary[category] = summary.get(category, 0) + amount

        print(f"{'Category':<20}{'Total Amount':<10}")
        print("-" * 30)
        for category, total in summary.items():
            print(f"{category:<20}{total:<10.2f}")

def main():
    """Main function to run the expense tracker."""
    expenses = load_expenses()

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Summary")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            expenses = add_expense(expenses)
            save_expenses(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            view_summary(expenses)
        elif choice == "4":
            save_expenses(expenses)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

