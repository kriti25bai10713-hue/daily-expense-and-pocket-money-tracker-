# entry.py

def create_entry(date, amount, type, category, note):
    """Return a formatted record string for an entry."""
    return f"{date},{amount},{type},{category},{note}\n"
