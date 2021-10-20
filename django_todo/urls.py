"""django_todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todo.views import get_todo_list  # Import todo.views get_todo_list function
from todo.views import add_item  # Import todo.views add_item function
from todo.views import edit_item  # Import todo.views edit_item function
from todo.views import toggle_item
from todo.views import delete_item

urlpatterns = [
    path('admin/', admin.site.urls),
    # Route todo.views with:
    # instead of giving a permanent url address like:
    # path('hello/', say_hello, name="hello")
    # we use:
    # blank url path (to act as homepage), responding function, identifier.
    path('', get_todo_list, name='get_todo_list'),
    # Routing for add item function in views.py
    # path to add_item.html with url link "add" and function add_item
    path('add', add_item, name='add'),
    # setting the path to point to edit_item.html with the item_id
    # This <angular> bracket syntax here is common in Django URLs.
    # And is the mechanism by which the item ID makes its way
    # from links or forms in our templates.
    # Through the URL and into the view which expects it as a parameter.
    path('edit/<item_id>', edit_item, name='edit'),
    # Routing for toggle function in views.py
    # copy paste from line above and change to toggle
    path('toggle/<item_id>', toggle_item, name='toggle'),
    # Routing for delete function in views.py
    path('delete/<item_id>', delete_item, name='delete')

]
