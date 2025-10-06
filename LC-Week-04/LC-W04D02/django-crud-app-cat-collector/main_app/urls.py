# main_app/urls.py

from django.urls import path
from . import views

# Import views to connect routes to view functions

urlpatterns = [
    # !- HW Extra SSOT - Single source of truth
    # Routes will be added here
    path("", views.home, name="home"),
    path("cats/", views.cat_index, name="cat-index"),
    path("about/", views.about, name="about"),
    # endpoint  cats/1 => cat_id:1    cats/2 => cat_id:2
    path("cats/<int:cat_id>/", views.cat_detail, name="cat-detail"),
    # path('/careers', views.career, name='home'),
    # !- HW 3.b Handle id for other endpoint dont have /blabla
    path('cats/create/', views.CatCreate.as_view(), name='cat-create'),
    path('cats/<int:pk>/update/', views.CatUpdate.as_view(), name='cat-update'),
    path('cats/<int:pk>/delete/', views.CatDelete.as_view(), name='cat-delete'),
]



# !- HW DJ- CBV read the links in the Materials
# STEPS:
# // !- 0- Problem variable inside the path
# 1- ULR: 'cats/5'
# 2- Interface (user interact with)
#  // !- DONE (what about cat.id)
# 3- Define the route
# 4- Create the view
# 5- Handle the response

""" 
Lecture Understanding
YS: 75% - 100%
>>: 50% - 75%
<<: 25% - 50%
NO: 00% - 25%
"""
