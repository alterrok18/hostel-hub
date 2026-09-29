from modules.expense import read_expenses

def show_stats():
    rows = read_expenses()
    if not rows:
        print("No expense data found.")
        return

    total = 0
    high = rows[0]
    pay = {}

    for x in rows:
        amt = float(x["amount"])
        total += amt

        if amt > float(high["amount"]):
            high = x

        name = x["paid_by"]
        pay[name] = pay.get(name, 0) + amt

    top = max(pay, key=pay.get)
    avg = total / len(rows)

    print("\n--- HOSTEL STATISTICS ---")
    print(f"Total spending: Rs. {total:.2f}")
    print(f"Number of expenses: {len(rows)}")
    print(f"Average expense: Rs. {avg:.2f}")
    print(f"Highest expense: {high['item']} - Rs. {float(high['amount']):.2f}")
    print(f"Most money paid by: {top} - Rs. {pay[top]:.2f}")

    print("\nSpending by payer:")
    for p, amt in pay.items():
        bars = max(1, int(amt / max(total, 1) * 20))
        print(f"{p:12} Rs. {amt:8.2f} " + "#" * bars)
