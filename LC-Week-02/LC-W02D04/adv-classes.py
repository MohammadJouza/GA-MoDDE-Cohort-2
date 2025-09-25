# O

print(
    ": ",
)

# !- HW
# Override
# Overwrite
# Abstraction
# Encapsulation
# Inheritance
# Polymorphism

num_1 = 4
num_2 = 6
# int class
print(type(num_2))
print("================ ")
print("2+3: ", num_1 + num_2)

print(":NUM:", dir(num_1))
""" 
behind the scene
def __add__(self , sec_value):
  return self.value + sec_value
 """

print("================ 33")


""" 
Human 
ft & Inch => KM
YS: KM M CM
NO: ft Inch
 """


class Distances_C2:
    def __init__(self, x=None, y=None):
        self.mt = x
        # money
        self.cm = y

    def __add__(self, sec_num):
        print("46 WE SHOULD HAVE THE ADD FUNCT HERE")
        print("ONLY calculate the meters")
        #  !- HW add mt.cm + mt.cm
        # reach them 3 + 5

        #    add them
        print("52 3: ", self.mt)
        print("53 5 : ", sec_num.mt)
        print("RESULT 54", self.mt + sec_num.mt)
        return self.mt + sec_num.mt

    #    print("================ ", sec_num)

    def __str__(self):
        return "" "MT:" + str(self.mt) + " CM:" + str(self.cm)

    # method give me the distance in readable human format (not Str)
    # 3.10 m
    def get_distance(self):
        print(f"the distance {self.mt}.{self.cm} Meter")

    # increase mt in mt instance
    def increase(self,amount):
        self.mt += amount
        print (f'TOTAL IS: {self.mt}')



#              mt  cm
d_1 = Distances_C2(3, 10)
d_2 = Distances_C2(5, 4)
# d1 + d2
"""  
d_1={    mt:3,    cm:3 }
d_2={    mt:5,    cm:4 }
"""
print("================ 54")
# call get_distance
# 3.10 m first d_1
# m cm
d_1.get_distance()
# summation Class / Object
print("================ SUM")
sum_1=d_1 + d_2
print("================ 84 ", sum_1)

# d_1.__add__(d_2)
print("================ ", 4 + 8)
# print("d1= {} d2={}".format(d1, d2))
# d3 = d1 + d2
# print(d3)



d_1.increase(50)
# d_1={    mt:3,    cm:3 }


