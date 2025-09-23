# fun1 / fun2
# 1
# 1.1
# 1.2
# 1.3

# 2
# 2.1
# 2.2
# 2.3

# 3
# 3.1
# 3.2
# 3.3

# 1
# 1
# 1

num_2 = 7


# return the num doubled
# parameters
def double_1(num_1):
    # bla bla
    # double the num_1
    return num_1 * 2


# invoke call execute
# arguments
# print("D:", double_1(5))
print("D:", double_1(10))
print("D:", double_1(num_2))


def first_function():
    pass


print("F1:", first_function())

# !- HW how we can
# 1- put default value
# 2- get rid of the error if we dont put arguments

# !- read more about the 'pass' statement


# Python
nums_1 = [1, 3, 2, 6, 5]
odds = list(filter(lambda num: num % 2, nums_1))
# variable odds
# list() built func - make a list
# filter(a1,a2) built func -
# a1 => func  True, False
# a2 => list
# filter(lambda num: num % 2, nums_1)
#

print(list(filter(lambda num: num % 2, nums_1)))


# three = list( filter(lambda num: num % 3, nums) )


# lambda num: num % 2, nums
# num:

# erro in Py
# print("R:", remi_2(4))


def remi_2(n_1):
    # num % 2
    return n_1 % 2 == 0


print("R:", remi_2(4))
nums_2 = [1, 3, 2, 6, 5]
even_1 = list(filter(lambda num: num % 2 == 1, nums_2))
print("E:", even_1)

# DN callback (func as arg)

#!- E.E.HW - JS hosting


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def compute(a, b, op):
    return op(a, b)


print("c:", compute(1, 2, add))


# list_2 = [ a,b,c]   ab]
# type = tuple
def func_4(*args):
    print("T:", type(args))
    for arg in args:
        print("ARG:", arg)


func_4(1, 2, "SEI")


# always print
# STU_1 : 1st arguments
# STU_2 : 2nd arguments
# then iterate over the rest
def func_5(a, b, *args):
    # print 1st and 2nd
    print("STU_1:", a)
    print("STU_2:", b)
    print("T:", type(args))
    # iterate over 3
    for arg in args:
        print("ARG:", arg)


func_5("Nezar", "Hayat", 34, "Full-Stack", True)

""" 
func_5("Nezar", "Hayat", 
34, "Full-Stack", True)

VOTE
YS: work
NO: error
<<: not work
>>: other 
 """

# !- HW: change tha name of *args and **kwargs


def divide_1(a, b):
    return f"{a} divided by {b} is {a / b}"


r_1 = divide_1(b=25, a=100)
r_2 = divide_1(a=100, b=25)

print(r_1)
print(r_2)


def dev_skills(dev_name, **kwargs):
    # kwargs will be a dictionary!
    dev = {"name": dev_name, "skills": kwargs}
    return dev


print(dev_skills("Karim", HTML=5, CSS=3, JavaScript=4, Python=2))


def arg_demo_3(pos1, pos2, *args, **kwargs):
    print(f"Positional params: {pos1}, {pos2}")
    print("*args:")
    for arg in args:
        print(" ", arg)
    print("**kwargs:")
    for keyword, value in kwargs.items():
        print(f"  {keyword}: {value}")


print("=========")
arg_demo_3("A", "B", 1, 2, 3, color="purple", shape="circle")


def add(a, b):
    return a + b


print("1:", add(10, 100.0))
# print('2:',add(10, '10'))
# print('3:',add(100))
# print(
#     "3.2:",
#     add(100, None),
# )
print("4:", add("abc", "def"))
# print("5:", add(10, 20, 30))
