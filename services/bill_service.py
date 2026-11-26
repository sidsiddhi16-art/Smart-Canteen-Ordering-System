def calculate_bill(items):
    """
    Calculate total bill amount.
    """
    grand_total = 0
    for item in items:
        quantity = item["quantity"]
        price = item["price"]
        total = quantity * price
        item["total"] = total
        grand_total += total
    return {
        "items": items,
        "grand_total": grand_total
    }
def get_bill_items():
    """
    Demo bill items.
    """
    items = [
        {
            "name": "Pizza",
            "quantity": 1,
            "price": 120
        },
        {
            "name": "Burger",
            "quantity": 2,
            "price": 80
        }
    ]

    return items