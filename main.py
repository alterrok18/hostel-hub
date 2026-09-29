from modules.expense import add_expense, show_expenses
from modules.settlement import show_balances
from modules.chores import show_chores, rotate_chores
from modules.items import add_item, borrow_item, return_item, show_items
from modules.analytics import show_stats
from modules.search import search_expenses

def menu():
    while True:
        print("\n" + "=" * 45)
        print("              HOSTELHUB")
        print("     Smart Hostel Utility Manager")
        print("=" * 45)
        print("1. Add expense")
        print("2. View expenses")
        print("3. View balances")
        print("4. View chores")
        print("5. Rotate chores")
        print("6. Add shared item")
        print("7. Borrow item")
        print("8. Return item")
        print("9. View shared items")
        print("10. Search expenses")
        print("11. Hostel statistics")
        print("0. Exit")

        ch = input("\nEnter choice: ").strip()

        if ch == "1":
            add_expense()
        elif ch == "2":
            show_expenses()
        elif ch == "3":
            show_balances()
        elif ch == "4":
            show_chores()
        elif ch == "5":
            rotate_chores()
        elif ch == "6":
            add_item()
        elif ch == "7":
            borrow_item()
        elif ch == "8":
            return_item()
        elif ch == "9":
            show_items()
        elif ch == "10":
            search_expenses()
        elif ch == "11":
            show_stats()
        elif ch == "0":
            print("\nThanks for using HostelHub!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
