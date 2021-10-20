from django.test import TestCase
# 3) for the third test we want to import Item to test data
from .models import Item


class TestViews(TestCase):

    # 1) we'll want to test that we can get the todo list which is the home page.
    def test_get_todo_list(self):
        # To test the HTTP responses of the views.
        # We can use a built-in HTTP client that comes with the Django testing framework.
        # I'll start with the get_todo_list view.
        # By setting a variable response equal to self.client.get
        # And providing the URL slash since we just want to get the home page.
        # We can then use assert equal to confirm that the response.status code is equal to 200
        # A successful HTTP response.
        # To confirm the view uses the correct template.
        # I'll use self.assertTemplateUsed and tell it the template we expect it to use in the response.
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    # 2) Then we'll want to test getting the add_item page.
    def test_get_add_item_page(self):
        # So moving on we can test getting the add_item page in the exact same way.
        # The only things we have to change are the URL we're getting.
        # And the template we expected to use.
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')

    # 3) And then test getting the edit_item page.

    def test_get_edit_item_page(self):
        # The Edit item page is a little different.
        # I'll paste in the same code and change the template we're expecting.
        # But, in this case, the URL will be edit followed by an item ID like 99 for example.
        # If we just pass it a static number though.
        # The test will only pass if that item ID exists in our database.
        # And we want to be more generic than that.
        # Conveniently in Django tests, we can also do crud operations.
        # So let's import the item model at the top. And then create an item to use in this test.
        item = Item.objects.create(name='Test Todo Item')
        # Now that we've got the item created.
        # Testing that we can get the Edit URL.
        # Is as simple as adding on its ID. Which I'll do with the Python f string.
        # if you're not familiar with f strings.
        # They work almost identically to the template literals you learned about in the JavaScript lessons.
        # All we've got to do is add an f before the opening quotation mark.
        # And then anything we put in curly brackets will be interpreted and turned into part of the string.
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    # 4) After that, we'll test that we can add an item.
    def test_can_add_item(self):
        # The last three tests will evaluate whether we are able to create update and delete items.
        # To test creating an item we can set the response equal to self.client.post on the add URL
        # And give it a name the item as if we've just submitted the item form.
        # If the item is added successfully. The view should redirect back to the home page.
        # So I'll use assert redirects. To confirm that it redirects back to slash.
        response = self.client.post('/add', {'name': 'Test Added Item'})
        self.assertRedirects(response, '/')

    # 5) Then test that we can delete an item using the delete view

    def test_can_delete_item(self):
        # Now let's test whether we can delete an item.
        # First I'll create one using item.objects.create.
        item = Item.objects.create(name='Test Todo Item')
        # And then I'll use the same syntax as we used on the edit_item view.
        # To make a get request. To delete slash the items ID
        response = self.client.get(f'/delete/{item.id}')
        # Again we'll want to assert that the view redirects us
        # as that's what it should do if it's successful.
        self.assertRedirects(response, '/')
        # And while we should technically already know the test passed at this point.
        # Just to prove that the item is in fact deleted.
        # I'll try to get it from the database using .filter and passing it the item ID
        existing_items = Item.objects.filter(id=item.id)
        # Since that item is the only one on the database and we just deleted it.
        # We can be certain the view works by asserting whether the length of existing items is zero.
        self.assertEqual(len(existing_items), 0)

    # 6) And finally we'll test we can toggle an item using the toggle view.
    def test_can_toggle_item(self):
        # The first three lines of this test will be almost the same.
        # So I'll copy those from above.
        # This time let's create an item with a done status of true.
        item = Item.objects.create(name='Test Todo Item', done=True)
        # Then call the toggle URL on its ID.
        response = self.client.get(f'/toggle/{item.id}')
        # After asserting that the view redirects us.
        self.assertRedirects(response, '/')
        # We can get the item again. And I'll call it updated item.
        updated_item = Item.objects.get(id=item.id)
        # And then use assert false to check it's done status.
        self.assertFalse(updated_item.done)

    # with that complete I'll run all the tests and verify that they all pass
    # With nine tests passing. In the next video we'll write one final test.

    # 7) Test post method of our edit view
    def test_can_edit_item(self):
        # First I'll create a new item like we've done above in the toggle item test.
        item = Item.objects.create(name='Test Todo Item')
        # Then let's grab the code above we use to test getting the edit view.
        # Except this time instead of using self.client.get We'll use self.client.post
        # And post an updated name.
        response = self.client.post(
            f'/edit/{item.id}', {'name': 'Updated Name'})
        # We'll then assert that the view redirected us.
        self.assertRedirects(response, '/')
        # And get the updated item just like we did above in the toggle item test.
        updated_item = Item.objects.get(id=item.id)
        # And now finally we can test that the updated items name is equal to updated name using assertEqual
        self.assertEqual(updated_item.name, 'Updated Name')
