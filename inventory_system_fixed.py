import json
from datetime import datetime

# Global variable
stock_data = {}

def add_item(item="default", qty=0, logs=None):
    """Add an item and its quantity to the inventory safely."""
    if logs is None:
        logs = []

    if not item:
        return

    # Validate quantity type
    if not isinstance(qty, int):
        print("Quantity must be an integer.")
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """Remove a specific quantity of an item from inventory."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        print(f"Item '{item}' not found in inventory.")


def get_qty(item):
    """Return the current quantity of an item."""
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """Load inventory data safely from a JSON file."""
    global stock_data
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
    except FileNotFoundError:
        print("No inventory data file found. Starting fresh.")


def save_data(file="inventory.json"):
    """Save inventory data safely to a JSON file."""
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f, indent=2)


def print_data():
    """Display all inventory items with their quantities."""
    print("Items Report")
    for i in stock_data:
        print(f"{i} -> {stock_data[i]}")


def check_low_items(threshold=5):
    """Return list of items whose quantity is below the threshold."""
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result


def main():
    """Demonstrate basic inventory operations."""
    add_item("apple", 10)
    add_item("banana", 2)
    remove_item("apple", 3)
    remove_item("orange", 1)
    print(f"Apple stock: {get_qty('apple')}")
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()
    print("eval removed for safety.")


if __name__ == "__main__":
    main()
