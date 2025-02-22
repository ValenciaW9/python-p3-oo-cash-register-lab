class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []

    def add_item(self, title, price, quantity=1):
        try:
            self.total += float(price) * quantity
        except ValueError:
            print(f"Invalid price: {price}")
        self.items.extend([title] * quantity)

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            self.total = round(self.total, 2)
            print(f"After the discount, the total comes to ${self.total:.2f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.items:
            last_price = self.items.pop()
            try:
                self.total -= float(last_price)
            except ValueError:
                print(f"Invalid price: {last_price}")