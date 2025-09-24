# account
class Account_3C:
    bank_name = "Etihad Bank"

    def __init__(self, name, amount):
        self.owner = name
        self.balance = amount

    def __add__(self, second_obj):
        return f"Total: {self.balance + second_obj.balance}"

    def __ge__(self, second_obj):
        print("GREATER OR EQUAL START:")
        if self.balance > second_obj.balance:
            print(f"{self.owner} has MORE money than {second_obj.owner}")
        else:
            print(f"{self.owner} has LESS money than {second_obj.owner}")

    # get me what inside the account (money)
    def check_balance(self):
        return f"Balance is : {self.balance}"

    # deposit
    def deposit(self, added_amount):
        self.balance += added_amount
        print(self.balance)
        return

    # withdraw
    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.balance:
            print("Noooooh, select another amount")
        else:
            self.balance -= withdraw_amount
            print(self.balance)
        return


# deposit

# account instance

Basil_a = Account_3C("Basil", 400)
# { owner:'Basil'   balance:400 }
Zeeb_a = Account_3C("Haitham", 5)
# { owner:'Haitham'   balance:5 }
print(Basil_a.check_balance())
print(Zeeb_a.check_balance())


Basil_a.deposit(5)
print(Basil_a.check_balance())

Basil_a.deposit(100)
print(Basil_a.check_balance())


Zeeb_a.withdraw(5)
print(Zeeb_a.check_balance())
print("================ 49")
Zeeb_a.withdraw(1)
print(Zeeb_a.check_balance())
Zeeb_a.deposit(100)
print(Zeeb_a.check_balance())
Zeeb_a.withdraw(1)
print(Zeeb_a.check_balance())

totalMoney = Zeeb_a + Basil_a
# Zeeb_a.__add__(Basil_a)
#                    504             + 3rd
#  1 + 5 + 6
#  6 + 6
print(totalMoney)
print(Zeeb_a.balance)  # 99
print(Basil_a.balance)  # 505
print("================ ")

Zeeb_a >= Basil_a

print(dir(Zeeb_a))
print("================ ")
print(Zeeb_a.bank_name)

class Student_5c:
    # class property
    course_name = "Python 3.0"
    __school_name = "General Assembly"

    def __init__(self, name, age):
        # instant level
        self.__name = name  # private instance attribute
        self.__age = age  # private instance attribute

        # age public
        # _age protected
        # __age private

    def __display(self):  # private method
        print("This is private method.")
    # Instance methods
    def checkName(self):
        return self.__name

    # Class methods
    @classmethod
    def calculate_age(cls, name, birth_year):
        # calculate age
        # return new object
        return cls(name, 2025 - birth_year)
        # return cls(name,date.today().year - birth_year)
        #     Student_5c("Rama",2025-2000)
        #     Student_5c("Rama",25)
    # Static methods
    @staticmethod
    def just_say_bla_bla():
        print("STATIC METHOD Bla Bla")

#           Student_5c("Rama",25)
student_7 = Student_5c("Ahmad", 22)
student_8 = Student_5c("Ali", 25)
rama_7 = Student_5c.calculate_age("Rama", 2000)
# rama_7 = {name }
print("================ ", rama_7.checkName())
#
# print(student_7.__school_name)
# print(student_7.__age)
# print(student_7.__name)
result_7 = student_7.checkName()
print("RRR:", result_7)
# print(student_7.__display())

print("PP:", student_7.course_name)
print("PP:", student_8.course_name)

student_7.just_say_bla_bla()

print()  # 505
print()  # 505
print()  # 505
print()  # 505
print()  # 505
print()  # 505
print()  # 505
