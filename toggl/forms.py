from django import forms

from toggl.initial_data import start_day, end_day


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class PasswordInput(forms.PasswordInput):
    input_type = 'password'


CHOICES = [('R', 'Takie same'),
           ('V', 'Różne')]


class EntryForm(forms.Form):
    use_required_attribute = False
    task = forms.CharField(label='Zadanie', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),
                           error_messages={'required': "Wpisz nazwę zadania"})
    date_start = forms.DateField(label='Początek zadania', widget=DateInput, initial=start_day,
                                 error_messages={'required': "Podaj datę początkową"})
    date_end = forms.DateField(label='Koniec zadania', widget=DateInput, initial=end_day,
                               error_messages={'required': "Podaj datę końcową"})
    different_hours = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect,
                                        error_messages={'required': "Zaznacz tryb pracy"})
    toggl_login = forms.EmailField(label='Login do konta Toggl', max_length=50,
                                   widget=forms.TextInput(attrs={'class': 'form-control'}),
                                   error_messages={'required': "Podaj login do konta Toggl",
                                                   'invalid': 'Podane dane nie są adresem email'})
    toggl_id_number = forms.IntegerField(label='Numer id konta Toggl',
                                         widget=forms.TextInput(attrs={'class': 'form-control'}),
                                         error_messages={'required': "Podaj numer id konta Toggl",
                                                         'invalid': 'Podany numer ID nie jest ciągiem cyfr'})
    toggl_password = forms.CharField(label='Hasło do konta Toggl', max_length=50,
                                     widget=PasswordInput(attrs={'class': 'form-control'}),
                                     error_messages={'required': "Podaj hasło do konta Toggl"})
    hour_start = forms.TimeField(label='Godzina rozpoczęcia', widget=TimeInput, required=False, initial="10:00")
    hour_end = forms.TimeField(label='Godzina zakończenia', widget=TimeInput, required=False, initial="18:00")
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
