# HostelHub

A simple command-line hostel utility manager built in Python.

HostelHub solves small but common hostel problems: splitting shared expenses, finding who owes whom, rotating chores, tracking borrowed items, searching expense records, and viewing simple spending statistics.

## Features
- Add and view shared expenses
- Calculate current balances and simple settlements
- Rotate hostel chores
- Track shared/borrowed items
- Search expense history
- Show basic spending statistics
- Save data in CSV/TXT files
- Validate important user inputs

## Why this project?
Hostel students often manage expenses, chores and shared belongings through memory or chat messages. HostelHub puts these tasks in one small offline program.

## Technologies
- Python 3
- Python standard library only
- CSV and TXT files
- Git and GitHub

No external Python packages are required.

## Run
1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

```bash
python main.py
```

## Project structure
```text
HostelHub/
├── main.py
├── modules/
│   ├── expense.py
│   ├── settlement.py
│   ├── chores.py
│   ├── items.py
│   ├── analytics.py
│   ├── search.py
│   └── validation.py
├── data/
├── tests/
├── docs/
├── screenshots/
├── README.md
├── statement.md
└── .gitignore
```

## Testing
Run:

```bash
python tests/test_hostelhub.py
```

Also test invalid menu choices, zero/negative amounts, duplicate items, missing items, and already-borrowed items.

## Python concepts used
Functions, variables, input/output, if/elif/else, while loops, for loops, lists, dictionaries, string operations, file handling, CSV handling, searching, counting, summation, maximum finding and list rotation.

## Screenshots
Add your final terminal screenshots inside the `screenshots` folder before submission.

## Future improvements
A GUI, login system, date-wise reports, categories, charts, and a database can be added later.
