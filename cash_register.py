#!/usr/bin/env python3
import io
import sys

class CashRegister:
    def __init__(self):
        self.total = 0
        self.items = []
        self.last_transaction_amount = 0
        self.discount = 0

    def add_item(self, title, price, quantity=1):
        item_total = price * quantity
        self.total += item_total
        self.items.extend([title] * quantity)
        self.last_transaction_amount = item_total

    def apply_discount(self):
        if self.discount > 0:
            self.total -= self.total * (self.discount / 100)
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.items:
            self.total -= self.last_transaction_amount
            self.items.pop()
            self.last_transaction_amount = 0
        else:
            print("No items to void.")

cash_register = CashRegister()
cash_register_with_discount = CashRegister()
cash_register_with_discount.discount = 20

def reset_register_totals():
    cash_register.total = 0
    cash_register_with_discount.total = 0

def test_discount_attribute():
    assert cash_register.discount == 0
    assert cash_register_with_discount.discount == 20

def test_total_attribute():
    assert cash_register.total == 0
    assert cash_register_with_discount.total == 0

def test_items_attribute():
    assert cash_register.items == []
    assert cash_register_with_discount.items == []

def test_add_item():
    cash_register.add_item("eggs", 0.98)
    assert cash_register.total == 0.98
    reset_register_totals()

def test_add_item_optional_quantity():
    cash_register.add_item("book", 5.00, 3)
    assert cash_register.total == 15.00
    reset_register_totals()

def test_add_item_with_multiple_items():
    cash_register.add_item("Lucky Charms", 4.5)
    assert cash_register.total == 4.5
    cash_register.add_item("Ritz Crackers", 5.0)
    assert cash_register.total == 9.5
    cash_register.add_item("Justin's Peanut Butter Cups", 2.50, 2)
    assert cash_register.total == 14.5
    reset_register_totals()

def test_apply_discount():
    cash_register_with_discount.add_item("macbook air", 1000)
    cash_register_with_discount.apply_discount()
    assert cash_register_with_discount.total == 800
    reset_register_totals()

def test_apply_discount_success_message():
    captured_out = io.StringIO()
    sys.stdout = captured_out
    cash_register_with_discount.add_item("macbook air", 1000)
    cash_register_with_discount.apply_discount()
    sys.stdout = sys.__stdout__
    assert captured_out.getvalue() == "After the discount, the total comes to $800.\n"
    reset_register_totals()

def test_apply_discount_reduces_total():
    cash_register_with_discount.add_item("macbook air", 1000)
    cash_register_with_discount.apply_discount()
    assert cash_register_with_discount.total == 800
    reset_register_totals()

def test_apply_discount_when_no_discount():
    captured_out = io.StringIO()
    sys.stdout = captured_out
    cash_register.apply_discount()
    sys.stdout = sys.__stdout__
    assert captured_out.getvalue() == "There is no discount to apply.\n"
    reset_register_totals()

def test_items_list_without_multiples():
    new_register = CashRegister()
    new_register.add_item("eggs", 1.99)
    new_register.add_item("tomato", 1.76)
    assert new_register.items == ["eggs", "tomato"]

def test_items_list_with_multiples():
    new_register = CashRegister()
    new_register.add_item("eggs", 1.99, 2)
    new_register.add_item("tomato", 1.76, 3)
    assert new_register.items == ["eggs", "eggs", "tomato", "tomato", "tomato"]

def test_void_last_transaction():
    cash_register.add_item("apple", 0.99)
    cash_register.add_item("tomato", 1.76)
    cash_register.void_last_transaction()
    assert cash_register.total == 0.99
    reset_register_totals()

def test_void_last_transaction_with_multiples():
    cash_register.add_item("tomato", 1.76, 2)
    cash_register.void_last_transaction()
    assert cash_register.total == 0.0
    reset_register_totals()