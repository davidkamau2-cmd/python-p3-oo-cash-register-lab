#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.total = 0
    self.discount = discount
    self.items = []
    self.last_transaction = 0

  def add_item(self, title, price, quantity=1):
    transaction_total = price * quantity
    self.total += transaction_total
    for _ in range(quantity):
      self.items.append(title)
    self.last_transaction = transaction_total

  def apply_discount(self):
    if self.discount == 0:
      print("There is no discount to apply.")
    else:
      # Calculate discounted total and ensure integer-like result when appropriate
      self.total = int(self.total * (100 - self.discount) / 100)
      print(f"After the discount, the total comes to ${self.total}.")

  def void_last_transaction(self):
    self.total -= self.last_transaction
    # If floating point rounding gives -0.0 or tiny negative, normalize to 0.0
    if abs(self.total) < 1e-9:
      self.total = 0.0