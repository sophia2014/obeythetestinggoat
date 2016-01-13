from selenium import webdriver

from .base import TodoFunctionalTest

class ToggleDoneTest(TodoFunctionalTest):

    def toggle_todo_done(self, todo_text):
        pass

    def check_marked_off(self, todo_text):
        pass

    def test_can_toggle_finished_items(self):
        self.browser.get(self.live_server_url)
        self.enter_a_new_item("Buy peacock feathers")
        self.enter_a_new_item("Buy fishing line")

        checkbox_selector = 'input[type="checkbox"]'
        checkboxes = self.browser.find_elements_by_css_selector(checkbox_selector)
        self.assertEqual(len(checkboxes), 2)

        self.toggle_todo_done("Buy peacock feathers")
        self.toggle_todo_done("Buy fishing line")

        current_list_url = self.browser.current_url
        self.browser.quit()

        self.browser = webdriver.Firefox
        self.browser.get(current_list_url)
        self.check_marked_off("Buy peacock feathers")
        self.check_marked_off("Buy fishing line")

        self.enter_a_new_item("Tie some flys")
        self.check_marked_off("Buy peacock feathers")
        self.check_marked_off("Buy fishing line")
        self.toggle_todo_done("Tie some flys")
        self.check_marked_off("Tie some flys")
