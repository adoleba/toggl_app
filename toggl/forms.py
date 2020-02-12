from django import forms

from toggl.initial_data import start_day, end_day


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class PasswordInput(forms.PasswordInput):
    input_type = 'password'


class EntryForm(forms.Form):
    task = forms.CharField(label='Zadanie', max_length=50)
    date_start = forms.DateField(label='Początek zadania', widget=DateInput, initial=start_day)
    date_end = forms.DateField(label='Koniec zadania', widget=DateInput, initial=end_day)
    toggl_login = forms.CharField(label='Login do konta Toggl', max_length=50)
    toggl_id_number = forms.IntegerField(label='Numer id konta Toggl')
    toggl_password = forms.CharField(label='Hasło do konta Toggl', max_length=50, widget=PasswordInput)
    hour_start = forms.TimeField(label='Godzina rozpoczęcia', widget=TimeInput, required=False, initial="10:00:00.00")
    hour_end = forms.TimeField(label='Godzina zakończenia', widget=TimeInput, required=False, initial="18:00:00.00")
    monday_hour_start = forms.TimeField(widget=TimeInput, required=False)
    monday_hour_end = forms.TimeField(widget=TimeInput, required=False)
    tuesday_hour_start = forms.TimeField(widget=TimeInput, required=False)
    tuesday_hour_end = forms.TimeField(widget=TimeInput, required=False)
    wednesday_hour_start = forms.TimeField(widget=TimeInput, required=False)
    wednesday_hour_end = forms.TimeField(widget=TimeInput, required=False)
    thursday_hour_start = forms.TimeField(widget=TimeInput, required=False)
    thursday_hour_end = forms.TimeField(widget=TimeInput, required=False)
    friday_hour_start = forms.TimeField(widget=TimeInput, required=False)
    friday_hour_end = forms.TimeField(widget=TimeInput, required=False)
