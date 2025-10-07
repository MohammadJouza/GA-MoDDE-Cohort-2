# main_app/views.py

from django.shortcuts import render,redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView 
# add these 

from django.http import HttpResponse
from .models import Cat,Toy

from .forms import FeedingForm


class CatCreate(CreateView):
    model = Cat
    # fields = "__all__"
    fields = [
        "name",
        "description",
        "age",
        "breed",
    ]


class CatUpdate(UpdateView):
    model = Cat
    # Let's disallow the renaming of a cat by excluding the name field!
    fields = ["breed", "description", "age"]


class CatDelete(DeleteView):
    model = Cat
    success_url = "/cats/"

class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'
# Define the home view function


class ToyList(ListView):
    model = Toy
    # {name: mouse, color: 'green'}
    # border-color:green

class ToyDetail(DetailView):
    model = Toy

class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']

class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def cat_index(request):
    cats = Cat.objects.all()
    return render(request, "cats/index.html", {"cats": cats})


def cat_detail(request, cat_id):
    # !- how can I get information from the urls
    cat = Cat.objects.get(id=cat_id)
    # !- HW 3.A Handle id for other cats dont have
    # toys = Toy.objects.all()  
    toys_cat_doesnt_have = Toy.objects.exclude(id__in = cat.toys.all().values_list('id'))

    # Fetch all toys
    # print("CAT_ID: ", cat_id)
    feeding_form = FeedingForm()
    return render(
        request, "cats/detail.html", {"cat": cat, "feeding_form": feeding_form, 'toys': toys_cat_doesnt_have}
    )

def add_feeding(request, cat_id):
    # create a ModelForm instance using the data in request.POST
    form = FeedingForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the cat_id assigned
        # {  date, meal    }
        new_feeding = form.save(commit=False)
        new_feeding.cat_id = cat_id
        new_feeding.save()
    return redirect('cat-detail', cat_id=cat_id)

def associate_toy(request, cat_id, toy_id):
    # Note that you can pass a toy's id instead of the whole object
    # Model.
    Cat.objects.get(id=cat_id).toys.add(toy_id)
    return redirect('cat-detail', cat_id=cat_id)
# !- HW 1- read about run the server without install all the packages
# !- HW 2- read about RESTful API

#  !- HW Read About csrf_token cross request / cross origin


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
