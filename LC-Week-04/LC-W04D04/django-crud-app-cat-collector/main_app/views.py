# main_app/views.py

from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView

# Add the two imports below
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Import the login_required decorator
from django.contrib.auth.decorators import login_required
# add these
# Import the mixin for class-based views
from django.contrib.auth.mixins import LoginRequiredMixin


from django.http import HttpResponse
from .models import Cat, Toy

from .forms import FeedingForm



# http://127.0.0.1:8000/?next=/cats/create/
class CatCreate(LoginRequiredMixin,CreateView):
    model = Cat
    # fields = "__all__"
    fields = [
        "name",
        "description",
        "age",
        "breed",
    ]

    # This inherited method is called when a
    # valid cat form is being submitted
    def form_valid(self, form):
        # form= {name. des, age,breed,user}
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user
        # print("AAA:",self.request.user)
        # form.instance is the cat
        # Let the CreateView do its job as usual
        return super().form_valid(form)


class CatUpdate(LoginRequiredMixin,UpdateView):
    model = Cat
    # Let's disallow the renaming of a cat by excluding the name field!
    fields = ["breed", "description", "age"]


class CatDelete(LoginRequiredMixin,DeleteView):
    model = Cat
    success_url = "/cats/"


class ToyCreate(LoginRequiredMixin,CreateView):
    model = Toy
    fields = "__all__"


# Define the home view function


class ToyList(LoginRequiredMixin,ListView):
    model = Toy
    # {name: mouse, color: 'green'}
    # border-color:green


class ToyDetail(LoginRequiredMixin,DetailView):
    model = Toy


class ToyUpdate(LoginRequiredMixin,UpdateView):
    model = Toy
    fields = ["name", "color"]


class ToyDelete(LoginRequiredMixin,DeleteView):
    model = Toy
    success_url = "/toys/"


# def home(request):
#     # return render(request, "index.html")
#     return render(request, "home.html")


class Home(LoginView):
    template_name = "home.html"


def about(request):
    return render(request, "about.html")

# HERE
@login_required
def cat_index(request):
    cats = Cat.objects.all()
    # print("ALL_CATS: ", cats)
    # cats = Cat.objects.filter(user=request.user)
    print("cats: ", cats)
    # You could also retrieve the logged in user's cats like this
    # cats = request.user.cat_set.all()
    return render(request, "cats/index.html", {"cats": cats})


def cat_detail(request, cat_id):
    # !- how can I get information from the urls
    cat = Cat.objects.get(id=cat_id)
    # !- HW 3.A Handle id for other cats dont have
    # toys = Toy.objects.all()

    toys_cat_doesnt_have = Toy.objects.exclude(id__in=cat.toys.all().values_list("id"))

    # Fetch all toys
    # print("CAT_ID: ", cat_id)
    feeding_form = FeedingForm()
    return render(
        request,
        "cats/detail.html",
        {"cat": cat, "feeding_form": feeding_form, "toys": toys_cat_doesnt_have},
    )

@login_required
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
    return redirect("cat-detail", cat_id=cat_id)

@login_required
def associate_toy(request, cat_id, toy_id):
    # Note that you can pass a toy's id instead of the whole object
    # Model.
    Cat.objects.get(id=cat_id).toys.add(toy_id)
    return redirect("cat-detail", cat_id=cat_id)


# !- HW 1- read about run the server without install all the packages
# !- HW 2- read about RESTful API

#  !- HW Read About csrf_token cross request / cross origin

@login_required
def remove_toy(request, cat_id, toy_id):
    # Look up the cat
    cat = Cat.objects.get(id=cat_id)
    # Look up the toy
    toy = Toy.objects.get(id=toy_id)
    # Remove the toy from the cat
    cat.toys.remove(toy)
    return redirect("cat-detail", cat_id=cat.id)


def signup(request):
    error_message = ""
    if request.method == "POST":
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in
            login(request, user)
            return redirect("cat-index")
        else:
            error_message = "Invalid sign up - try again"
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {"form": form, "error_message": error_message}
    return render(request, "signup.html", context)
    # Same as:
    # return render(
    #     request,
    #     'signup.html',
    #     {'form': form, 'error_message': error_message}
    # )


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
