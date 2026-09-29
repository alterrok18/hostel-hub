import csv
from pathlib import Path
from modules.validation import get_num, get_names

FILE = Path(__file__).parent.parent / "data" / "expenses.csv"

def add_expense():
    item = input("Expense name: ").strip().title()
    if not item:
        print("Expense name cannot be empty.")
        return

    amt = get_num("Amount: Rs. ")
    paid = input("Paid by: ").strip().title()
    people = get_names("Shared by (comma separated): ")

    if not paid:
        print("Payer name cannot be empty.")
        return

    share = amt / len(people)

    with open(FILE, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow([item, f"{amt:.2f}", paid, "|".join(people), f"{share:.2f}"])

    print(f"Saved. Each person's share: Rs. {share:.2f}")

def read_expenses():
    rows = []
    if not FILE.exists():
        return rows

    with open(FILE, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            rows.append(row)
    return rows

def show_expenses():
    rows = read_expenses()
    if not rows:
        print("No expenses found.")
        return

    print("\n--- EXPENSE HISTORY ---")
    for i, x in enumerate(rows, 1):
        print(f"{i}. {x['item']} | Rs. {float(x['amount']):.2f} | Paid by {x['paid_by']}")
        print("   Shared by:", x["people"].replace("|", ", "))
