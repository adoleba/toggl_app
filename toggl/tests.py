import datetime

from django.http import HttpRequest
from django.test import TestCase, Client, RequestFactory
from django.urls import resolve
from django.utils.html import escape

from toggl.views import dates_for_first_week_days_in_month, dates_between_date_end_and_date_start
from toggl.forms import EntryForm
from toggl.initial_data import start_day, end_day
from toggl.views import done, EntryView

correct_toggl_dict = {'task': 'test', 'date_start': '2020-02-01', 'date_end': '2020-02-29', 'different_hours': 'R',
                      'hour_start': '10:00', 'hour_end': '18:00', 'toggl_login': 'edfrgthyuj@wp.pl',
                      'toggl_password': 'swdefr', 'toggl_id_number': '2345'}

incorect_toggl_dict = {'task': '', 'date_start': '2020-02-01', 'date_end': '2020-02-29', 'different_hours': 'R',
                       'toggl_login': 'swdefr', 'toggl_id_number': '2345'}


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


class EntryViewTest(TestCase):
    def setUp(self):
        self.request = RequestFactory().get('/')
        self.form = EntryForm()

    def test_view_in_template_context(self):
        view = EntryView()
        view.setup(self.request)
        context = view.get_context_data()
        self.assertIn('view', context)

    def test_render_input_form_in_template(self):
        view = EntryView.as_view()
        response = view(self.request)
        content = response.rendered_content
        self.assertIn('input', content)

    def test_render_buttons_for_hours_choice(self):
        view = EntryView.as_view()
        response = view(self.request)
        content = response.rendered_content
        self.assertIn('btn-group', content)

    def test_render_send_button_form_in_template(self):
        view = EntryView.as_view()
        response = view(self.request)
        content = response.rendered_content
        self.assertIn('button', content)

    def test_form_has_initial_start_day(self):
        self.assertEqual(self.form['date_start'].initial, start_day())

    def test_form_has_initial_end_day(self):
        self.assertEqual(self.form['date_end'].initial, end_day())

    def test_task_field_form_has_class_from_widget(self):
        self.assertIn('class="form-control"', self.form['task'].as_widget())


class EntryFormValidationTest(TestCase):
    def setUp(self):
        self.correct_form = EntryForm(data=correct_toggl_dict)
        self.incorrect_form = EntryForm(data=incorect_toggl_dict)

    def test_valid_form_is_correct_validated(self):
        self.assertTrue(self.correct_form.is_valid())
        self.assertFalse(not self.correct_form.is_valid())

    def test_invalid_form_is_correct_validated(self):
        self.assertFalse(self.incorrect_form.is_valid())
        self.assertTrue(not self.incorrect_form.is_valid())

    def test_error_if_toggl_password_not_entered(self):
        self.assertEqual(self.incorrect_form.errors['toggl_password'], ['Podaj hasło do konta Toggl'])

    def test_toggl_login_as_not_email(self):
        self.assertEqual(self.incorrect_form.errors['toggl_login'], ['Podane dane nie są adresem email'])


class EntryViewFunctionTest(TestCase):
    def setUp(self):
        self.test_valid_data = {'task': 'test', 'date_start': datetime.date(2020, 2, 1),
                                'date_end': datetime.date(2020, 2, 29), 'different_hours': 'R',
                                'toggl_login': 'edfrgthyuj@wp.pl', 'toggl_id_number': 2345,
                                'toggl_password': 'sdf', 'hour_start': datetime.time(10, 0),
                                'hour_end': datetime.time(18, 0), 'monday_hour_start': None, 'monday_hour_end': None,
                                'tuesday_hour_start': None, 'tuesday_hour_end': None, 'wednesday_hour_start': None,
                                'wednesday_hour_end': None, 'thursday_hour_start': None, 'thursday_hour_end': None,
                                'friday_hour_start': None, 'friday_hour_end': None}

        self.first_week_days_in_month = dates_for_first_week_days_in_month(self.test_valid_data)

        self.working_days = dates_between_date_end_and_date_start(self.first_week_days_in_month, self.test_valid_data)

    def test_hour_end_for_regular_and_variable_hours(self):
        if self.test_valid_data['different_hours'] == 'R':
            self.assertFalse(None, self.test_valid_data['hour_end'])
        else:
            self.assertTrue(not None, self.test_valid_data['hour_end'])

    def test_duration_in_sec_is_correct(self):
        duration_in_sec = (self.test_valid_data['hour_end'].hour - self.test_valid_data['hour_start'].hour) * 3600
        self.assertEqual(duration_in_sec, 28800)

    def test_first_monday_is_correct(self):
        monday = datetime.date(2020, 1, 27)
        self.assertEqual(monday, self.first_week_days_in_month['first_monday'])

    def test_day_earlier_than_date_start(self):
        day = datetime.date(2020, 1, 28)
        self.assertNotIn(day, self.working_days)

    def test_day_later_than_date_end(self):
        day = datetime.date(2020, 3, 27)
        self.assertNotIn(day, self.working_days)
