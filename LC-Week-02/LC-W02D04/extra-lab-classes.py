# Shawarma Stand Simulator
class ShawarmaStand:
    def __init__(self, name, meat_type="chicken"):
        self.name = name
        self.meat_type = meat_type
        self.orders = []
        self.is_open = False

    def open(self):
        self.is_open = True
        print(f"{self.name} is now OPEN! Yalla Shawarma!")

    def close(self):
        self.is_open = False
        print(f"{self.name} is now CLOSED. Come back tomorrow!")

    def add_order(self, customer_name):
        if self.is_open:
            order = f"{customer_name} ordered {self.meat_type} Shawarma"
            self.orders.append(order)
            print(order)
        else:
            print(f"Sorry {customer_name}, {self.name} is closed!")

    def show_orders(self):
        print(f"\nOrders for {self.name}:")
        for o in self.orders:
            print("-", o)

    def __str__(self):
        return f"Shawarma Stand '{self.name}' serving {self.meat_type}."
"""  
👉 Extra twist:

1- Add price per Shawarma and calculate total sales.

2- Add an option for “extra toum” 🧄 or “spicy” 🌶️.

3- Add inheritance → e.g., FalafelStand(ShawarmaStand).
"""