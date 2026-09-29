import csv
import tempfile
from pathlib import Path
import modules.expense as expense
import modules.settlement as settlement

def test_balances():
    old = expense.FILE
    old2 = settlement.read_expenses
    try:
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "expenses.csv"
            with open(f, "w", newline="", encoding="utf-8") as out:
                w = csv.writer(out)
                w.writerow(["item", "amount", "paid_by", "people", "share"])
                w.writerow(["Dinner", "400.00", "Aryan", "Aryan|Rahul", "200.00"])
            expense.FILE = f
            settlement.read_expenses = expense.read_expenses
            bal = settlement.get_balances()
            assert round(bal["Aryan"], 2) == 200.00
            assert round(bal["Rahul"], 2) == -200.00
    finally:
        expense.FILE = old
        settlement.read_expenses = old2

if __name__ == "__main__":
    test_balances()
    print("Test passed.")
