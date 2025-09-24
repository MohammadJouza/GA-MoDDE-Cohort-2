nums = [1, 2, 3]

print("NUMS: ", nums)
print("NUMS: ", dir(nums))

nums.append(4)

print("NUMS: ", nums)

# magic methods


print("================ 1")


# CatInTheStreet
class Cat_C1:
    # ___ later
    # self
    def __init__(self, name_1, owner, age=0):
        # print("NAME: ", name_1)
        self.animal_name = name_1
        # self.propertyName
        self.age = age
        self.owner = owner

    def meow(self):
        print(f"{self.animal_name} says meeeow!")

    # result - new method to change the owner
    # create a method  (newOnwer)
    def change_owner(self, new_owner_name):
        # change the owner
        self.owner = new_owner_name
        # optional - print
        print(f"the owner change to become: {self.owner}")

    def __str__(self):
        return f"Cat     ---- named {self.animal_name} is {self.age} years old"


# create an object from class
# instances
cat_1 = Cat_C1("Jojo", "Sarah")
cat_2 = Cat_C1("Fahmeh", "Hamza", 2)

print("CAT_1.NAME: ", cat_1.animal_name)

print(cat_1)
# print("CAT_1: ", dir(cat_1))
# var / propert
print("CAT_1.age: ", cat_1.age)
print("CAT_2.age: ", cat_2.age)
cat_2.meow()
# print("45 CAT_2.meow: ", cat_2.meow())
# print("46 CAT_2.meow: ", cat_1.meow())
# listName[index]
# objName.propertyName
# objName.method()
# self => objName


print("================ 222")

print("cat_1.owner before : ", cat_1.owner)
cat_1.change_owner("Purvi")
print("cat_1.owner after: ", cat_1.owner)
print("cat_1: ", cat_1)

# print("aa: ", cat_1.callMe())
print("cat_1 AFTER STR: ", cat_1)


# Override
# Overwrite



