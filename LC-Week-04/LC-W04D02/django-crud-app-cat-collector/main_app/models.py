from django.db import models

# Create your models here.
# models = tables

class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    
# cat_1 = Cat()
# record  Table
# c = Cat(name='Biscuit', breed='Sphinx', description='Cuddle monster. Hairless.', age=2)


""" 
try:
    id_s= 2
    cat = Cat.objects.get(id=id_s)
except Cat.DoesNotExist:
    # Handle the case where the object does not exist
    print(f"This cat: {id_s} - does not exist!")

try:
    id_s= 1
    cat = Cat.objects.get(id=id_s)
    print(f"This cat: {id_s} - IS EXIST!")
except Cat.DoesNotExist:
    # Handle the case where the object does not exist
    print(f"This cat: {id_s} - does not exist!")



Cat.objects.filter(age=2)


Cat.objects.filter(age=0)
Cat.objects.filter(age__gte=1)

Cat.objects.order_by('-name')

 """