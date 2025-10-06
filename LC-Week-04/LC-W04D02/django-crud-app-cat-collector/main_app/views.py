# main_app/views.py

from django.shortcuts import render

# Create your views here.
# Import HttpResponse to send text-based responses
from django.http import HttpResponse
from .models import Cat

# Define the home view function
def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def cat_index(request):
    cats = Cat.objects.all()
    return render(request, "cats/index.html", {"cats": cats})

def cat_detail(request,cat_id):
    # !- how can I get information from the urls
    cat = Cat.objects.get(id=cat_id)
    # !- HW 3.A Handle id for other cats dont have
    # print("CAT_ID: ", cat_id)
    return render(request, "cats/detail.html", {"cat": cat})


# !- HW 1- read about run the server without install all the packages
# !- HW 2- read about RESTful API
""" 
class Cat:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age


# {name: "" , breed: "" , description: "", age: ""}
# Create a list of Cat instances
cats = [
    Cat("Momo", "tabby", "Kinda rude.", 3),
    # {name: "Lolo" , breed: "tabby" , description: "Kinda rude", age: 3}
    Cat("Sachi", "tortoiseshell", "Looks like a turtle.", 0),
    Cat("Fancy", "bombay", "Happy fluff ball.", 4),
    Cat("Bonk", "selkirk rex", "Meows loudly.", 6),
]



# def sum(x,y):
#     return x+y

# sum() user enter /sum

 """