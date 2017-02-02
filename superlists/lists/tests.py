from django.test import TestCase

# Create your tests here.

class HomePageTest(TestCase):

    def test_home_page_is_about_todo_lists(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')