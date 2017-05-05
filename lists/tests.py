from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')  # find appropriate view function
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(),
                         expected_html)  # decode converts response bytes into unicode string, previously we compared bytes
        # self.assertIn(b'<title>To-Do lists</title>', response.content)
        # self.assertTrue(response.content.endswith(b'</html>'))
        # self.assertTrue(response.content.strip().endswith(b'</html>')) (if problem with

# class Smoke(TestCase):
#     def test_bad_maths(self):
#         self.assertEqual(1 + 1, 3)
