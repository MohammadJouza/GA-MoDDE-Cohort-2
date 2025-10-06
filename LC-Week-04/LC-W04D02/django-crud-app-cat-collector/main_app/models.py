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
YS: Workflow 10
NO: Steps 7
<<: Materials 0
>>: 
 """


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




""" 
GET
STEPS to create page for creating new cat
// - interface
// - url 'cat/create'
!- CatCreate
- html page that has (form)
!- form
- route
- template
- response user

==========
POST
- input (fill data)
- hit the button (send POST)
- handle (model) - database

 """