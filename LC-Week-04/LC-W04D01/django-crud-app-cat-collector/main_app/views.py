# main_app/views.py

from django.shortcuts import render

# Create your views here.
# Import HttpResponse to send text-based responses
from django.http import HttpResponse


# Define the home view function
def home(request):
    # Send a simple HTML response
    # return HttpResponse('<h1>Basil Cat ᓚᘏᗢ</h1>')
    return render(request, "index.html")


def about(request):
    # return HttpResponse('<h1>About the cats</h1>')
    return render(request, "about.html")


def cat_index(request):
    # return HttpResponse('<h1>About the cats</h1>')
    #                             name of variable : value
    return render(request, "cats/index.html", {"cats": cats})


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