# importing render and redirect
from django.shortcuts import render, redirect, get_object_or_404
# first we import Items from .models
# this allows us to use item model in our views
from .models import Item
from .forms import ItemForm

# Create your views here.


# READ items function
def get_todo_list(request):
    # Query set of all the items in the database
    # creating variable items equal to Item.objects.all()
    # returns all items from the database
    # the request parameter is the basic read argument to read form database
    items = Item.objects.all()
    # Then we create variable context which is a dictionary with all items in it
    # which we are going to access in the in our html template file
    # Once we save this we have created the communication between our
    # frontend and the backend
    context = {
        'items': items
    }
    # and then we have to add the context as a third argument to the render function
    # to make it accessible in our todo_list.html
    return render(request, 'todo/todo_list.html', context)


# CREATE, add items function
# here we are just giving the function the name of add_item
def add_item(request):
    if request.method == 'POST':
        # name = request.POST.get('item_name')
        # done = 'done' in request.POST
        # Item.objects.create(name=name, done=done)
        # return redirect('get_todo_list')
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    form = ItemForm()
    # Create a context which contains the empty form.
    context = {
        'form': form
    }
    # and add the page name that needs to be rendered add_item.html
    return render(request, 'todo/add_item.html', context)


# EDIT item function
# passing request AND item_id from our template as parameter
def edit_item(request, item_id):
    # here we get a copy of the item from the database
    # we can do this using a built in Django shortcut called get_object_or_404
    # which we'll use to say we want to get an instance of the item model
    # with an ID equal to the item ID that was passed into the view via the URL
    # This method will either return the item if it exists. Or a 404 page not found if not.
    item = get_object_or_404(Item, id=item_id)
    # HERE WE CAN COPY THE POST STATEMENTS FROM add_item FUNCTION
    # AND JUST HAVE TO CHANGE OR ADD THE instance=item AS PARAMETER
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    # Then just like above we'll create an instance of our item form
    # and return it to the template in the context.
    # To pre-populate the form with the items current details.
    # We can pass an instance argument to the form (instance=item) that we have declared on the line above.
    # Telling it that it should be prefilled with the information for the item
    # we just got from the database.
    form = ItemForm(instance=item)
    # Create a context which contains the empty form.
    context = {
        'form': form
    }
    # this returns/ renders the edit_item.html template
    # and add the form context to the template
    return render(request, 'todo/edit_item.html', context)


# TOGGLE item, instead of clickng the done button
def toggle_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.done = not item.done
    item.save()
    return redirect('get_todo_list')


# DELETE view function
def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    # I'll start by copying the toggle item view.
    # But instead of changing the item status and saving it.
    # I'll simply delete the item and then redirect.
    item.delete()
    return redirect('get_todo_list')
