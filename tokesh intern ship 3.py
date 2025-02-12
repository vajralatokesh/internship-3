import json, os
from datetime import datetime

data_file = "expenses.json"

def load_expenses():
    return json.load(open(data_file)) if os.path.exists(data_file) else []

def save_expenses(expenses):
    json.dump(expenses, open(data_file, "w"), indent=4)

def add_expense(amount, category, description):
    expenses = load_expenses()
    expenses.append({"amount": amount, "category": category, "description": description, "date": datetime.now().isoformat()})
    save_expenses(expenses)
    print("Expense added successfully!")

def view_summary():
    expenses, summary = load_expenses(), {}
    for exp in expenses:
        summary[exp['category']] = summary.get(exp['category'], 0) + exp['amount']
    for cat, total in summary.items():
        print(f"Total spent on {cat}: ${total}")

def main():
    while (choice := input("1.Add 2.View 3.Exit: ")) != "3":
        if choice == "1": add_expense(float(input("Amount: ")), input("Category: "), input("Description: "))
        elif choice == "2": view_summary()
        else: print("Invalid choice")

if __name__ == "__main__":
    main()
