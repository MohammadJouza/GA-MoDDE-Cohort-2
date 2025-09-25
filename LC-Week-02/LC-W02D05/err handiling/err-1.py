import sys

print("================ hello")


# avg 3 nums and gis us the avg
def avg(num_1, num_2, num_3):
    # total
    result_1 = num_1 + num_2 + num_3
    # divide that by the num of the par
    return result_1 / 3


print(1, avg(5, 3, 1))  # => 3
print(2, avg(6, 4, 2))  # => 4

# we have an exception
# print(3, avg(30, '10', 20))  # => 20

print(4, avg(30, 10, 20))  # => 20

# try: this code
# except: if error
# else:good no error
# finally:
print("================ 1111")
# varible = func(1,2)
# file_object = open("/user/ecommerce/data.csv", "r")

print("30: ", 30)

try:
    file_1 = open("/user/ecommerce/data.csv", "r")
except FileNotFoundError:
    print("ARE YOU SURE THE PATH IS CORRECT")

# a = 5
# b = 0
# print(a / b)

try:
    a = 5
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("cant divide by ZERO")

print("30: ", 40)
test_1 = True

while test_1:
    try:
        # var = int conver str to numb
        # input: take for the user
        x = int(input("PLEASE ENTER A NUMBER: "))
    except ValueError:
        print("PLEASE ENTER A VALID NUMBER! ...")
    else:
        print(f"{x} SQUARED IS {x * x}")
        test_1 = False
    finally:
        print("HAVE A GOOD DAY")
    print("Last line in While")


print("================ 222")
print()
print()
print()
