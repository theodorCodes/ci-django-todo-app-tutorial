# 1) import django forms to access form functionality
from django import forms
# 2) import our database item model
from .models import Item

# Our form will be a class that inherits a built-in Django class to give it some basic functionality.
# To set it up we need to create a new class ItemForm
# In the brackets we specify from which upper class we inherit from
# and we inherit from our imported class forms.ModelForm where we
# get the functionality from


class ItemForm(forms.ModelForm):
    # here we create an inner class Meta
    # This inner class just gives our form some information about itself.
    # Like which fields it should render how it should display error messages and so on.
    class Meta:
        # In this class the only thing I'm going to define is our model.
        # Which is going to be our item model.
        model = Item
        # And fields which will tell it we want to display the name in done fields from the model.
        # The idea of creating this form in Django is that rather than writing an
        # entire form ourselves in HTML.
        # We can simply render it out as a template variable.
        fields = ['name', 'done']
