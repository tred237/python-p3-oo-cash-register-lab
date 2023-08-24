#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0
    self.items = list()
    self.transactions = list()

  def add_item(self, item, price, quantity = 1):
    self.total += price * quantity
    for i in range(quantity):
      self.items.append(item)
    self.transactions.append({
      'item': item,
      'price': price,
      'quantity': quantity,
    })

  def apply_discount(self):
    if (self.discount != 0):
      self.total = int(self.total * (1 - self.discount / 100))
      print(f"After the discount, the total comes to ${self.total}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    voided_transaction = self.transactions.pop()
    del self.items[-abs(voided_transaction['quantity']):]
    if (self.discount != 0):
      self.total -= (voided_transaction['price'] * voided_transaction['quantity']) * (1 - self.discount / 100)
    else:
      self.total -= (voided_transaction['price'] * voided_transaction['quantity'])