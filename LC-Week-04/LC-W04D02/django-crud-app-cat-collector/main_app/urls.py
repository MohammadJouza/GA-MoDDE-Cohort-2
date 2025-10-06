# main_app/urls.py

from django.urls import path
from . import views 
# Import views to connect routes to view functions

urlpatterns = [
    # Routes will be added here
    path('', views.home, name='home'),
    path('cats/', views.cat_index, name='cat-index'),
    path('about/', views.about, name='home'),
    # endpoint  cats/1 => cat_id:1    cats/2 => cat_id:2
    path('cats/<int:cat_id>/', views.cat_detail, name='cat-index'),
    # path('/careers', views.career, name='home'),
    # !- HW 3.b Handle id for other endpoint dont have /blabla
]
 

# STEPS:
# // !- 0- Problem variable inside the path 
# 1- ULR: 'cats/5'
# 2- Interface (user interact with)
#  // !- DONE (what about cat.id)
# 3- Define the route
# 4- Create the view
# 5- Handle the response

