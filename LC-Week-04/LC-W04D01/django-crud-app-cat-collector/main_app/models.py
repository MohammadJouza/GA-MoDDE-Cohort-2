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
