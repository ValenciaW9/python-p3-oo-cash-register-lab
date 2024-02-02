class CashRegister:
    def __init__(self):
        self.items = []
        self.total = 0
        self.discount = 0

    def add_item(self, item_name, price, quantity):
        self.items.append({"item_name": item_name, "price": price, "quantity": quantity})
        self.total += price * quantity

    def calculate_total(self):
        return self.total

    def apply_discount(self, discount_percentage):
        if discount_percentage < 0 or discount_percentage > 100:
            return "Invalid discount percentage"
        self.total -= (self.total * discount_percentage) / 100

    def void_last_transaction(self):
        if not self.items:
            return "No items to void"
        last_item = self.items.pop()
        self.total -= last_item["price"] * last_item["quantity"]