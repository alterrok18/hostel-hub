from modules.expense import read_expenses

def search_expenses():
    key = input("Search expense: ").strip().lower()
    found = []

    for x in read_expenses():
        text = x["item"] + " " + x["paid_by"] + " " + x["people"]
        if key in text.lower():
            found.append(x)

    if not found:
        print("No matching expense found.")
        return

    print(f"\nFound {len(found)} record(s):")
    for x in found:
        print(f"{x['item']} | Rs. {float(x['amount']):.2f} | Paid by {x['paid_by']}")
