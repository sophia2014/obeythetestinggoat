from .base import TodoFunctionalTest
from unittest import skip

class ItemValidationTest(TodoFunctionalTest):
    @skip("Haven't implemented this.")
    def test_cannot_add_empty_list_item(self):
        self.fail("Finish the test!")
