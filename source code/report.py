# report.py

def show_entries(entries):
    print("\n--- All Entries ---")
    for line in entries:
        date, amount, type, category, note = line.strip().split(",", 4)
        print(f"{date} | {type.upper():7} | ₹{amount:6} | {category:10} | {note}")
    print("-------------------")

def show_summary(entries):
    total_expense = 0.0
    total_income = 0.0
    for line in entries:
        date, amount, type, category, note = line.strip().split(",", 4)
        amount = float(amount)
        if type == "expense":
            total_expense += amount
        elif type == "income":
            total_income += amount
    print(f"Total Income:  ₹{total_income}")
    print(f"Total Expense: ₹{total_expense}")
    print(f"Balance:       ₹{total_income - total_expense}")
