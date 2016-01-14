from .base import TodoFunctionalTest

class ItemValidationTest(TodoFunctionalTest):

    def test_cannot_add_empty_list_item(self):
        self.browser.get(self.live_server_url)
        self.enter_a_new_item('')

        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        self.enter_a_new_item('Buy milk')
        self.check_for_row_in_list_table('Buy milk')

        self.enter_a_new_item('')
        self.check_for_row_in_list_table('Buy milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        self.enter_a_new_item('Make tea')
        self.check_for_row_in_list_table('Buy milk')
        self.check_for_row_in_list_table('Make tea')
