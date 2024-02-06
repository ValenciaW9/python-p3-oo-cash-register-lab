#!/usr/bin/env python3


class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0.0
        self.items = []
        self.last_transaction = []

    def add_item(self, name, price, count=1):
        for i in range(count):
            self.items.append(name)
        self.total += price * count
        self.last_transaction = [name, price, count]

    def apply_discount(self):
        if self.discount != 0:
            self.total *= 1 - self.discount / 100
            print(f"After the discount, the total comes to ${self.total:g}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_transaction[1] * self.last_transaction[2]
