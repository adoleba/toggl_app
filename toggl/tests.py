from django.http import HttpRequest
from django.test import TestCase, Client
from django.urls import resolve
from django.utils.html import escape

from toggl.forms import EntryForm
from toggl.views import done


correct_toggl_dict = {'task': 'test', 'date_start': '2020-02-01', 'date_end': '2020-02-29', 'different_hours': 'R',
                   'hour_start': '10:00', 'hour_end': '18:00', 'toggl_login': 'edfrgthyuj@wp.pl',
                   'toggl_password': 'swdefr', 'toggl_id_number': '2345'}


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


class MainPageTestGet(TestCase):
    def setUp(self):
        self.client = Client()
        self.response = self.client.get('/')

    def test_used_template_is_correct(self):
        self.assertTemplateUsed(self.response, 'toggl/index.html')

    def test_status_code_is_200(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template_is_not_empty(self):
        self.assertNotEqual(self.response.context, "None")

    def test_form_in_context(self):
        self.assertIsInstance(self.response.context['form'], EntryForm)


class MainPageTestPost(TestCase):
    def setUp(self):
        self.client = Client()

    def test_task_error_if_form_empty(self):
        response = self.client.post('/')
        expected_error = escape('Wpisz nazwę zadania')
        self.assertContains(response, expected_error)

    # long time
    def test_redirect_after_correct_post(self):
        response = self.client.post('/', data=correct_toggl_dict)
        self.assertRedirects(response, '/done/')
