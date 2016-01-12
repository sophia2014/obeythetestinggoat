from selenium import webdriver

from .base import TodoFunctionalTest

class NewVisitorTest(TodoFunctionalTest):

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get(self.live_server_url)
        self.assertIn('To-Do', self.browser.title)

        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        self.enter_a_new_item('Buy peacock feathers')

        edith_list_url = self.browser.current_url
        self.assertRegexpMatches(edith_list_url, '/lists/.+')

        self.check_for_row_in_list_table('1. Buy peacock feathers\nDelete')

        self.enter_a_new_item('Use peacock feathers to make a fly')

        self.check_for_row_in_list_table('1. Buy peacock feathers\nDelete')
        self.check_for_row_in_list_table('2. Use peacock feathers to make a fly\nDelete')

        self.browser.quit()

        self.browser = webdriver.Firefox()
        self.browser.get(self.live_server_url)

        page_text = self.browser.find_element_by_tag_name('body').text

        self.assertNotIn('Buy peacock feathers\nDelete', page_text)
        self.assertNotIn('make a fly\nDelete', page_text)

        self.enter_a_new_item('Buy milk')

        francis_list_url = self.browser.current_url
        self.assertRegexpMatches(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers\nDelete', page_text)
        self.assertIn('Buy milk\nDelete', page_text)
