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
