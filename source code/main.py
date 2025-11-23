# main.py

from entry import create_entry
from storage import save_entry, load_entries
from report import show_entries, show_summary
from menu import show_menu, get_user_input

def run():
    print("=== DAILY EXPENSE & POCKET MONEY TRACKER ===")
    while True:
        show_menu()
        choice = input("Choose option: ").strip()
        if choice == '1':
            args = get_user_input()
            entry_str = create_entry(*args)
            save_entry(entry_str)
            print("Entry added.")
        elif choice == '2':
            entries = load_entries()
            show_entries(entries)
        elif choice == '3':
            entries = load_entries()
            show_summary(entries)
        elif choice == '4':
            print("Tracker closed. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Uncomment the below line only for interactive use.
# run()
