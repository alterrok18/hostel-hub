# 🏠 HostelHub

**Who paid for the maggi? Whose turn is it to clean? Who has my extension board?**
HostelHub answers all three from your terminal.

It's a small offline Python program for people who share a room, a PG, or a flat. It keeps track of shared expenses, chores and borrowed stuff so nobody has to scroll through the group chat to find out.

![Python](https://img.shields.io/badge/Python-3-blue) ![Dependencies](https://img.shields.io/badge/dependencies-none-brightgreen) ![Storage](https://img.shields.io/badge/storage-CSV%20%2F%20TXT-lightgrey)

---

## 💡 Why I made this

In a hostel, everything shared runs on memory. Food bills, grocery runs, who did the dishes last, who borrowed the iron. It works until it doesn't.

I wanted one simple tool that keeps all of this in one place, works without internet, and is easy enough that I can explain every line of it.

---

## ✨ What it does

| | Feature | In short |
|---|---|---|
| 💸 | **Expenses** | Add a bill, pick who shared it, and the split is worked out for you |
| ⚖️ | **Balances** | See who should get money and who owes, with simple settlement suggestions |
| 🧹 | **Chores** | View the chore list and rotate it so everyone gets a turn |
| 📦 | **Shared items** | Add items, borrow them, return them, and always know who has what |
| 🔍 | **Search** | Find any past expense by item, payer or person |
| 📊 | **Statistics** | Total spent, average, biggest expense, and how much each person paid |

Everything is saved in plain CSV/TXT files, so your data is still there when you close the program.

---

## 🚀 Getting started

You only need Python 3. There's nothing to install.

```bash
git clone https://github.com/<your-username>/HostelHub.git
cd HostelHub
python main.py
```

You'll see this menu:

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

Type a number, press Enter, and follow the prompts.

---

## 🗂️ How it's organised

Each feature lives in its own small file, and `main.py` just shows the menu and calls the right one.

```text
HostelHub/
├── main.py              # the menu
├── modules/
│   ├── expense.py       # add and view expenses
│   ├── settlement.py    # balances and who pays whom
│   ├── chores.py        # view and rotate chores
│   ├── items.py         # shared items: add, borrow, return
│   ├── search.py        # search expenses
│   ├── analytics.py     # statistics
│   └── validation.py    # checks user input
├── data/                # saved CSV / TXT files
├── tests/               # test_hostelhub.py
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

## 🧠 How the maths works

**Balances:** for every expense, the person who paid is credited the full amount, and everyone sharing it is charged their share. After going through all expenses, a positive balance means "gets money back" and a negative one means "owes money".

**Settlement:** the program then matches people who owe with people who should receive, until everything evens out.

**Chore rotation:** the last chore moves to the front of the list, so everyone shifts by one.

---

## 🛡️ What it won't let you do

The program checks your input so it doesn't crash or save nonsense:

- Zero or negative amounts are rejected
- Invalid menu choices show a message and bring the menu back
- The same shared item can't be added twice
- An item that's already borrowed can't be borrowed again
- Borrowing an item that doesn't exist is rejected

---

## 🧪 Testing

```bash
python tests/test_hostelhub.py
```

This checks the balance calculation. I tested the rest by hand, going through the menu with wrong inputs: bad menu options, zero and negative amounts, duplicate items, missing items and already-borrowed items.

---

## 📸 Screenshots

Screenshots of the running program are in the [`screenshots`](screenshots/) folder.

---

## 🔮 What I'd add next

- Dates and categories for expenses
- Monthly charts and reports
- Accounts, so multiple rooms can use it
- A simple GUI
- A database instead of files

---

## 📚 Concepts used

Functions, loops, conditionals, lists, dictionaries, string handling, file and CSV handling, searching, counting, summing, finding the maximum, and list rotation. Built for **CSE1021, Introduction to Problem Solving and Programming**.
