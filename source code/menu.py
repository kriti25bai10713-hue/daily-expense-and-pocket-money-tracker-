# menu.py

def show_menu():
    print("\n1. Add Entry\n2. View Entries\n3. Summary\n4. Exit")

def get_user_input():
    date = input("Date (YYYY-MM-DD): ").strip()
    amount = input("Amount (₹): ").strip()
    type = input("Type (expense/income): ").strip().lower()
    category = input("Category (food, gift, etc.): ").strip()
    note = input("Note: ").strip()
    return date, amount, type, category, note
