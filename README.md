# 🏠 HostelHub

Who paid for the maggi? Whose turn is it to clean? Who has my extension board?
HostelHub answers all three from your terminal.

It's a small offline Python program for people sharing a room, PG, or flat. It keeps tracks of shared expenses, chores and borrowed stuff so that no one has to go through the group chat to find out.

![Python](https://img.shields.io/badge/Python-3-blue) ![Dependencies](https://img.shields.io/badge/dependencies-none-brightgreen) ![Storage](https://img.shields.io/badge/storage-CSV%20%2F%20TXT-lightgrey)
---

## 💡 Why did I make this

In a hostel, everything that is shared is handled through memory. Bills, grocery shopping, who washed the dishes, who borrowed the iron. This goes on until it doesn't.

I wanted a single tool that could keep track of all this information, work offline, and be simple enough that I could explain every line of its code.
---
## ✨ Features

| | Feature | In short |
|---|---|---|
| 💸 | Expenses | Add an expense with who shared in the cost and the share is calculated automatically |
| ⚖️ | Balances | See who gets money and who pays, with simple suggestions to settle the balances |
| 🧹 | Chores | View chore list, and rotate it so everyone takes a turn |
| 📦 | Shared items | Add items, borrow them, return them, always know who has what |
| 🔍 | Search | Find any expense in the past by item, payer or person |
| 📊 | Statistics | View total spent, average, biggest expense, and how much each person paid |

All the information is stored in CSV/TXT files so that it persists even after the program has exited.
---

## 🚀 Getting started

You only need Python 3.

```bash
git clone https://github.com//HostelHub.git
cd HostelHub
python main.py
```

You will see this menu:

```text
=============================================
HOSTELHUB
Smart Hostel Utility Manager
=============================================
1. Add expense
2. View expenses
3. View balances
4. View chores
5. Rotate chores
6. Add shared item
7. Borrow item
8. Return item
9. View shared items
10. Search expenses
11. Hostel statistics
0. Exit
```

Enter an option and press Enter, then follow the prompts.
---
## 🗂️ Organisation

Each feature has its own module and `main.py` is just the menu and a switch-case to call the right one.

```text
HostelHub/
├── main.py       # the menu
├── modules/
│  ├── expense.py    # add and view expenses
│  ├── settlement.py  # balances and who pays whom
│  ├── chores.py    # view and rotate chores
│  ├── items.py     # shared items: add, borrow, return
│  ├── search.py    # search expenses
│  ├── analytics.py   # statistics
│  └── validation.py  # checks user input
├── data/        # saved CSV / TXT files
├── tests/        # test_hostelhub.py
├── docs/
├── screenshots/
├── README.md
├── statement.md
└── requirements.txt
```

| File | What it stores |
|---|---|
| `expenses.csv` | item, amount, paid_by, people, share |
| `items.csv` | item, owner, borrowed_by |
| `chores.txt` | name and chore |
---

## 🧠 How the calculations work

Balances: for every expense, the person who paid is credited the full amount, and everyone sharing in the expense is debited their share. After all expenses are processed, positive balances are those who get money, and negative balances are those who pay.

Settlement: The program pairs up people who owe with people who are owed, until all balances are settled.

Chore rotation: The last chore moves to the front of the list, so everyone gets a turn.
---

## 🛡️ What the program guards against
The program takes care of erroneous input to prevent crashing:
- Zero or negative amounts are not allowed
- Choice other than numbers in the menu prompt are ignored and the menu is shown again
- A shared item may not be added twice
- An item that is already borrowed may not be borrowed again
- Borrowing an item that does not exist is not allowed
---
## 🧪 Testing
```bash
python tests/test_hostelhub.py
```
The test checks the correctness of the balance calculation. I tested the rest of the program manually by entering all the possible wrong input: bad menu option, amounts, zero, negative, duplicate items, etc.
---
## 📸 Screenshots
Inside the [`Screenshots`](Screenshots/) folder.
---
## 🔮 Future improvements

- Date and category for expenses
- Monthly charts and reports
- Accounts, so that people in different rooms can use the same program
- A graphical interface
- A database to replace CSV files
---

## 📚 Concepts used

Functions, loops, conditionals, lists, dictionaries, string handling, file and CSV handling, searching, counting, summing, finding the maximum, and list rotation. This project is for CSE1021, Introduction to Problem Solving and Programming.
