from django.contrib import admin
# Here we import item
from .models import Item
# And this says from the current directories models file
# we want to import the item class.


# Register your models here.


# And then we're going to use the admin.site.register function.
# To actually register our item model.
admin.site.register(Item)
