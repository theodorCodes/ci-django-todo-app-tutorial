# I'll begin in test_models.py By as usual importing TestCase from django.test
from django.test import TestCase
# And we'll need to import our item model from .models
from .models import Item


# Now I'll create a new class called TestModels which inherits TestCase.
class TestModels(TestCase):

    # And inside it a method called test_done_defaults_to_false
    def test_done_defaults_tp_false(self):
        # This test is extremely simple.
        # All we need to do is create an item. Using item.objects.create
        # And I'll call this item Test Todo Item.
        item = Item.objects.create(name='Test Todo Item')
        # And then use assert false. To confirm that it's done status is in fact, false by default
        self.assertFalse(item.done)

    # Create Missing String Test
    # create a new test called test_item_string_method_returns_name
    def test_item_string_method_returns_name(self):
        # I'll use item.objects.create
        # To create an item with the name of Tests Todo Item.
        item = Item.objects.create(name='Test Todo Item')
        # And then use self.assertEqual to confirm
        # that this name is returned when we render this item as a string.
        self.assertEqual(str(item), 'Test Todo Item')
