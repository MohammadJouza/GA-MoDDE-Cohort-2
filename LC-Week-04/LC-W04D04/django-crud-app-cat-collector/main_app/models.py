from django.db import models
from django.urls import reverse

# Create your models here.
# models = tables

# Add the Toy model
class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("toy-detail", kwargs={"pk": self.id})


class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    # Add the M:M relationship
    toys = models.ManyToManyField(Toy)

    def __str__(self):
        return self.name

    # Define a method to get the URL for this particular cat instance
    def get_absolute_url(self):
        # Use the 'reverse' function to dynamically find the URL for viewing this cat's details
        return reverse("cat-detail", kwargs={"cat_id": self.id})


MEALS = (("B", "Breakfast"), ("L", "Lunch"), ("D", "Dinner"))


class Feeding(models.Model):
    date = models.DateField("FEEDING DATE")
    meal = models.CharField(
        max_length=1,
        # add the 'choices' field option
        choices=MEALS,
        # set the default value for meal to be 'B'
        default=MEALS[0][0],
        # Breakfast
    )
    # Django will add _id
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_meal_display()} on {self.date}"

    # Define the default order of feedings
    class Meta:
        ordering = ["-date"]
        # This line makes the newest feedings appear first




""" 
Cat



cats= [
Cat(1,2,'',.ii)
Cat(1,2,'',.ii)
Cat(1,2,'',.ii)
Cat(1,2,'',.ii)

]
 """

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
