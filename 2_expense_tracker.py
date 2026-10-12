# project 2: expense tracker
# add your spending, then see how much you spent in total and per category.


import csv
import os

FILE_NAME = "expenses.csv"


def load_expenses():
    # each expense is a dictionary like {"category": "food", "amount": 4.5}
    expenses = []

    if not os.path.exists(FILE_NAME):
        return expenses

    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # amounts are saved as text, so turn them back into numbers
            expenses.append({                "category": row["category"],
                "amount": float(row["amount"]),
            })
    return expenses


def save_expenses(expenses):
    with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["category", "amount"])
        writer.writeheader()
        writer.writerows(expenses)


def add_expense(expenses):
    category = input("category (for example food, travel, fun): ").strip().lower()
    if category == "":
        print("the category can't be empty")
        return

    # try to turn what the user typed into a number
    try:
        amount = float(input("amount in pounds: "))
    except ValueError:
        print("please type a number such as 4.50")
        return

    if amount <= 0:
        print("the amount must be more than 0")
        return

    expenses.append({"category": category, "amount": amount})
    save_expenses(expenses)
    print("expense added")


def show_summary(expenses):
    if len(expenses) == 0:
        print("no expenses yet")
        return

    # add up the amounts for each category using a dictionary
    totals = {}
    for expense in expenses:
        category = expense["category"]
        if category in totals:
            totals[category] = totals[category] + expense["amount"]
        else:
            totals[category] = expense["amount"]

    total_spent = sum(expense["amount"] for expense in expenses)

    print()
    print("spending by category:")
    # sort so the biggest category comes first
    for category, amount in sorted(totals.items(), key=lambda item: item[1], reverse=True):
        print(f"  {category}: £{amount:.2f}")

    print()
    print(f"total spent: £{total_spent:.2f}")
    print(f"number of expenses: {len(expenses)}")


def main():
    expenses = load_expenses()

    while True:
        print()
        print("1) add an expense")
        print("2) show summary")
        print("3) quit")
        choice = input("choose 1-3: ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_summary(expenses)
        elif choice == "3":
            print("tracker closed!")
            break
        else:
            print("please choose 1, 2 or 3")


if __name__ == "__main__":
    main()
