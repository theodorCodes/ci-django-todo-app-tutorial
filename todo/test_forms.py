# In test forms.py I'll begin by importing Testcase from django.test
from django.test import TestCase
# and our item form from .forms
from .forms import ItemForm

# Now let's create a new class called TesItemForm.


class TestItemForm(TestCase):

    # We'll begin with the simple test to make sure that the name field is required
    # in order to create an item.
    # In general, you'll want to name your tests so that when they fail you can easily see what the issue is.
    # So I'll call this one test item name is required.
    def test_item_name_is_required(self):
        # I'll begin by instantiating a form and we'll deliberately instantiate it without a name
        # to simulate a user who submitted the form without filling it out.
        form = ItemForm({'name': ''})
        # This form should not be valid.
        # So I'll use assert false to ensure that that's the case.
        self.assertFalse(form.is_valid())
        # When the form is invalid it should also send back a dictionary of fields on which
        # there were errors and the Associated error messages
        # Knowing this we can be even more specific by using assert in to assert
        # whether or not there's a name key in the dictionary of form errors.
        self.assertIn('name', form.errors.keys())
        # Finally to really drive the point home.
        # I'll use assert equal to check whether the error message on the name field
        # is this field is required.
        # Remember to include the period at the end here as the string will need to match exactly.
        # Also just a note we're using the zero index here
        # because the form will return a list of errors on each field.
        # And this verifies that the first item in that list is
        # our string telling us the field is required.
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_field_is_not_required(self):
        form = ItemForm({'name': 'Test Todo Item'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])
