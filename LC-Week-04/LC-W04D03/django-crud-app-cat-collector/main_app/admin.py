from django.contrib import admin

# Register your models here.
from .models import Cat, Feeding

admin.site.register(Cat)
admin.site.register(Feeding)

# python manage.py makemigrations
# python manage.py migrate



