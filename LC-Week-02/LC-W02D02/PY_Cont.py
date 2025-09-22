#
# nodemon

num_1 = 1

print("num_1:", num_1)
ccc = "course"

stu_1 = {
    "name": "Abd",
    ccc: "GA Full-Stack",
    "age": 24,
    "hair-color": "black",
    "status": "Meh",
}

print("stu_1:", stu_1)
# CRUD: Create Read Update Delete

#  [ ] square bracket {} curly bracket () parentheses
print("NAME:", stu_1["name"])
stu_1["name"] = "whatever"

print("NAME:", stu_1["name"])

print("N/A:", stu_1.get("skills"))
# !- 1- HW read more about GET method

# for
# the var you want to give for each tme the key change
# in
# obj_name
for key in stu_1:
    # print(1)
    # obj_name[name_key]
    print("KEY:", key, "| VALUE:", stu_1[key])

# !- 2- HW: print("KEY", key)
# !- 3- HW: `if` with `in`
# HW for Zeeb - f"{}"

# dic_name[key_name] = value  (no # no "")
stu_1["has_driver_license"] = False

# del dic_name[key_name]
del stu_1["age"]
print(stu_1)
# for sure that the age [property is not there]
# print(stu_1["age"])
# dic_name.get(key_name)
print("N/A:", stu_1.get("age"))

#        012345
str_1 = "Sawsan"
print("BLA:", len(str_1))

print("STU:", len(stu_1))
print("STU:", stu_1)

# var      = dict_name.items()
dict_items = stu_1.items()
print(dict_items)

num_2 = 5
for key, val in stu_1.items():
    print(f"K:{key} = V: {val} | {num_2}")


""" 
YS: 5
NO: error
<<: 4
>>: 6
CF: Other
 """

""" 
stu_1 = { "name": "Abd", ccc: "GA Full-Stack",
"age": 24, "hair-color": "black", "status": "Meh",}
 """


animals_1 = ["Cat", "Bee", "Momo", "Penguin"]
#              0      1      2         3
# list[index]

print(animals_1)
print(animals_1[2])
# -1    length - 1
print(animals_1[-2])

print(animals_1)
# re assign
#      =           | num_2 = 7   num_2=9
animals_1[1] = "Sheep"
print(animals_1)

# animals_1 = ["Cat", "Bee", "Momo", "Penguin"]
# Syntax  list_name.append(new_item)
animals_1.append("Dog")
print(animals_1)
# list_name.insert(inx,value)
animals_1.insert(1, "Wolf")
print(animals_1)

#
animals_1.pop(2)  # Sheep
print(animals_1)
del animals_1[1]  # wolf
print(animals_1)
# animals_1.remove("Wolf")

print(animals_1)

nums_1 = [3, 6, 9, 12, 15]
print(nums_1)

# add one to each one
# for one_num in nums_1:
#   # range / counter
#   print(one_num)
#   # nums_1[one_num] += one_num+1
#   nums_1[one_num] +=1


for i_2, elem in enumerate(nums_1):
    print(f"i_2: {i_2}, E: {elem}")
# nums_1 = [3,4, 6, 9, 12, 15]
#        i / value
# 0 3 => 1 4 => 2 6
print(nums_1)

print(enumerate(nums_1))


# !- HW 4 - 💪 Lists & Dictionary - Practice Exercise (10 mins)

nums_2 = [1, 2, 3, 4, 5]
#         1  4  9  16 25
print(nums_2)

# an empty list =
nums_3 = []

# iterate over each elem inside the list
for elem_2 in nums_2:
    # elem_2 represent the index
    # multiple each elem
    # stor that in num_3
    # list_name.append(value)
    nums_3.append(elem_2 * elem_2)

print(nums_3)

squares_3 = [n * n for n in nums_2]
# nums_2 = [1, 2, 3, 4, 5]
print("S3:", squares_3)
plus_1 = [n + 1 for n in nums_2]
print("S3:", plus_1)

# bring for me the list of hte even num
even_2 = [elem for elem in nums_2 if elem % 2 == 0]
print("even_2:", even_2)
# nums_2 = [1, 2, 3, 4, 5]
colors = ("red", "green", "blue")
r, g, b = colors
print("3 V:", r, g, b)

# this is what we did with hte dict before
# for key, val in stu_1.items():
#     print(f"{key} = {val}")

#             sequence start:end:step
short_name = "Alexandria"[0:4]
#             0123456789
print(short_name)

print(nums_3)
# [1, 4, 9, 16, 25]
short_num = nums_3[2:]
print(short_num)


#


#

#
