# 🧪 Lab: Shawarma Stand – OOP Access & Methods

## 🎯 Learning Goals
By the end of this lab, you should be able to:
- Differentiate between **public**, **protected**, and **private** members.
- Use **instance methods** vs **class methods** vs **static methods**.
- Understand **encapsulation** in a fun, real-world example.

## ⚙️ Setup
You already have the base code for `ShawarmaStand`.  
We’ll extend it step by step. Create a file named `shawarma_lab.py` and copy the starting code into it:

```python
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
````


## Part 1: Public, Protected, and Private Members

1- Inside ShawarmaStand, add:

    A public attribute price = 2.5 (price per shawarma, visible to everyone).

    A protected attribute _secret_recipe = "7 spices mix".

    A private attribute __bank_code = "1234JD".

2- Add a method get_bank_code() that returns the bank code safely.

3- Test your code:
```python
stand = ShawarmaStand("Abu Ali")
print(stand.price)            # ✅ accessible
print(stand._secret_recipe)   # ⚠️ possible, but not polite
print(stand.get_bank_code())  # ✅ safe access to private
```

❓ Discussion: Why do we pretend not to touch _secret_recipe even though Python lets us?

## Part 2: Instance Methods

- Add an instance method calculate_bill(self, quantity)
    → returns quantity * self.price.

Example:
```python
stand = ShawarmaStand("Abu Ali")
print(stand.calculate_bill(3))   # -> 7.5
```

## Part 3: Class Methods

1- Add a class variable total_sales = 0 (shared across all stands).

2- Add a class method:
```python
@classmethod
def add_sales(cls, amount):
    cls.total_sales += amount
```

3- Update add_order() so that when a shawarma is ordered, it calls ShawarmaStand.add_sales(self.price).

Test:
```python
stand1 = ShawarmaStand("Abu Ali")
stand1.open()
stand1.add_order("Ahmad")
stand1.add_order("Laila")

stand2 = ShawarmaStand("Falafel King")
stand2.open()
stand2.add_order("Mohammad")

print("Total sales across all stands:", ShawarmaStand.total_sales)
```

## Part 4: Static Methods

Add a static method:
```python
@staticmethod
def convert_to_jod(dollars):
    return round(dollars / 1.41, 2)
```

Example:
```python
print(ShawarmaStand.convert_to_jod(10))  # -> ~7.09 JOD
```

## 🧆 Bonus Challenges

1- Add inheritance:
```python
class FalafelStand(ShawarmaStand):
    def __init__(self, name):
        super().__init__(name, meat_type="falafel")
```

2- Modify calculate_bill() to handle extra toum 🧄 (+0.25) and spicy 🌶️ (+0.10).

3- Add a __str__() method that shows shop name, meat type, and total orders.