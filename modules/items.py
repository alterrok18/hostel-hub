import csv
from pathlib import Path

FILE = Path(__file__).parent.parent / "data" / "items.csv"

def read_items():
    rows = []
    if not FILE.exists():
        return rows
    with open(FILE, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    return rows

def save_items(rows):
    with open(FILE, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["item", "owner", "borrowed_by"])
        w.writeheader()
        w.writerows(rows)

def add_item():
    item = input("Item name: ").strip().title()
    owner = input("Owner: ").strip().title()

    if not item or not owner:
        print("Item and owner cannot be empty.")
        return

    rows = read_items()
    for x in rows:
        if x["item"].lower() == item.lower():
            print("This item already exists.")
            return

    rows.append({"item": item, "owner": owner, "borrowed_by": ""})
    save_items(rows)
    print("Item added.")

def borrow_item():
    item = input("Item to borrow: ").strip()
    name = input("Borrowed by: ").strip().title()
    rows = read_items()

    for x in rows:
        if x["item"].lower() == item.lower():
            if x["borrowed_by"]:
                print("Item is already borrowed.")
                return
            x["borrowed_by"] = name
            save_items(rows)
            print("Borrowing recorded.")
            return

    print("Item not found.")

def return_item():
    item = input("Item to return: ").strip()
    rows = read_items()

    for x in rows:
        if x["item"].lower() == item.lower():
            if not x["borrowed_by"]:
                print("Item is already available.")
                return
            x["borrowed_by"] = ""
            save_items(rows)
            print("Item returned.")
            return

    print("Item not found.")

def show_items():
    rows = read_items()
    if not rows:
        print("No shared items found.")
        return

    print("\n--- SHARED ITEMS ---")
    for x in rows:
        if x["borrowed_by"]:
            print(f"{x['item']} | Owner: {x['owner']} | With: {x['borrowed_by']}")
        else:
            print(f"{x['item']} | Owner: {x['owner']} | AVAILABLE")
