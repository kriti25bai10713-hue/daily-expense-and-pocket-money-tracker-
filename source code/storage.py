# storage.py

DATA_FILE = "expenses.txt"

def save_entry(entry_str):
    with open(DATA_FILE, "a") as f:
        f.write(entry_str)

def load_entries():
    try:
        with open(DATA_FILE, "r") as f:
            return f.readlines()
    except FileNotFoundError:
        return []
