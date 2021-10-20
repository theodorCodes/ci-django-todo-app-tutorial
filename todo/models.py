from django.db import models

# The imported models library, imports the model's folder from
# the model's folder from the Django/DB directory in our project
# site-packages. And through that we gain access to everything
# in that folder, just like when we imported our view function
# in urls.py
# Here you can see how Django model works by importing all
# required model files:
# https://github.com/django/django/blob/main/django/db/models/__init__.py

# Create your models here.


# Django will automatically create a database table called Item
# when seeing that we have created a Item() class, after we
# run the migration command
class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    # here we overwrite, redefine the particular line 527 shown at source file
    # to represent the name of each item in the todo list
    def __str__(self):
        return self.name
