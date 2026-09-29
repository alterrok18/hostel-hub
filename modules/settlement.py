from modules.expense import read_expenses

def get_balances():
    bal = {}

    for x in read_expenses():
        amt = float(x["amount"])
        paid = x["paid_by"]
        people = x["people"].split("|")
        share = amt / len(people)

        if paid not in bal:
            bal[paid] = 0
        bal[paid] += amt

        for p in people:
            if p not in bal:
                bal[p] = 0
            bal[p] -= share

    return bal

def get_settlements():
    bal = get_balances()
    give = [[p, -a] for p, a in bal.items() if a < -0.01]
    take = [[p, a] for p, a in bal.items() if a > 0.01]
    ans = []

    i = 0
    j = 0

    while i < len(give) and j < len(take):
        amt = min(give[i][1], take[j][1])
        ans.append((give[i][0], take[j][0], amt))
        give[i][1] -= amt
        take[j][1] -= amt

        if give[i][1] < 0.01:
            i += 1
        if take[j][1] < 0.01:
            j += 1

    return ans

def show_balances():
    bal = get_balances()
    if not bal:
        print("No expense data found.")
        return

    print("\n--- CURRENT BALANCES ---")
    for p, a in bal.items():
        if a > 0.01:
            print(f"{p}: should receive Rs. {a:.2f}")
        elif a < -0.01:
            print(f"{p}: owes Rs. {-a:.2f}")
        else:
            print(f"{p}: settled")

    print("\n--- SIMPLE SETTLEMENT ---")
    ans = get_settlements()
    if not ans:
        print("Everyone is settled.")
    else:
        for a, b, n in ans:
            print(f"{a} -> {b}: Rs. {n:.2f}")
