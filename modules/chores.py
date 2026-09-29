from pathlib import Path

FILE = Path(__file__).parent.parent / "data" / "chores.txt"

def read_lines():
    if not FILE.exists():
        return []
    with open(FILE, encoding="utf-8") as f:
        return [x.strip() for x in f if x.strip()]

def show_chores():
    rows = read_lines()
    if not rows:
        print("No chores found.")
        return

    print("\n--- CHORE LIST ---")
    for i, x in enumerate(rows, 1):
        name, chore = x.split(",", 1)
        print(f"{i}. {name} -> {chore}")

def rotate_chores():
    rows = read_lines()
    if len(rows) < 2:
        print("At least two chore entries are needed.")
        return

    names = []
    jobs = []

    for x in rows:
        name, chore = x.split(",", 1)
        names.append(name)
        jobs.append(chore)

    jobs = jobs[-1:] + jobs[:-1]

    with open(FILE, "w", encoding="utf-8") as f:
        for i in range(len(names)):
            f.write(names[i] + "," + jobs[i] + "\n")

    print("Chores rotated successfully.")
    show_chores()
