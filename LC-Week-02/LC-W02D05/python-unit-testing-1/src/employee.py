# src/employee.py

class Company:
    def __init__(self, company):
        self.company = company
        print(f"Welcome to {self.company}")

class Employee(Company):
    """Employee class"""

    def __init__(self, first, last, company="General Assembly"):
        super().__init__(company)

        self.first = first
        self.last = last
    
    @property
    def email(self):
        return f'{self.first}{self.last}@email.com'

    @property
    def fullname(self):
        return f'{self.first.capitalize()} {self.last.capitalize()}'
    
    def get_company_info(self):
        return f"{self.fullname} works at {self.company}"
    