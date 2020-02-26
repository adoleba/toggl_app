from django.http import HttpRequest
from django.test import TestCase, Client
from django.urls import resolve

from toggl.views import done


class DonePageTest(TestCase):
    def setUp(self):
        self.request = HttpRequest()
        self.response = done(self.request)

    def test_url_complies_with_path_for_view(self):
        link = resolve('/done/')
        self.assertEqual(link.func, done)

    def test_end_of_template_with_html_marker(self):
        self.assertTrue(self.response.content.endswith(b'</html>'))

    def test_beginning_of_template_with_doctype_html_marker(self):
        self.assertIn(b'<!DOCTYPE html>', self.response.content)


class DonePageTestWithClient(TestCase):
    def setUp(self):
        self.client = Client()
        self.response = self.client.get('/done/')

    def test_used_template_is_correct(self):
        self.assertTemplateUsed(self.response, 'toggl/done.html')

    def test_status_code_is_200(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template_is_not_empty(self):
        self.assertNotEqual(self.response.context, "None")
