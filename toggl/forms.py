from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class PasswordInput(forms.PasswordInput):
    input_type = 'password'


class EntryForm(forms.Form):
    task = forms.CharField(label='Zadanie', max_length=50)
    date_start = forms.DateField(label='Początek zadania', widget=DateInput)
    date_end = forms.DateField(label='Koniec zadania', widget=DateInput)
    toggl_login = forms.CharField(label='Login do konta Toggl', max_length=50)
    toggl_id_number = forms.IntegerField(label='Numer id konta Toggl', )
    toggl_password = forms.CharField(label='Hasło do konta Toggl', max_length=50, widget=PasswordInput)
    different_hours = forms.BooleanField(label='Czy godziny pracy są różne w poszczególne dni tygodnia?')
    hour_start = forms.TimeField(label='Godzina rozpoczęcia - ', widget=TimeInput)
    hour_end = forms.TimeField(label='Godzina zakończenia', widget=TimeInput)
    monday_hour_start = forms.TimeField(label='Godzina rozpoczęcia - poniedziałek', widget=TimeInput)
    monday_hour_end = forms.TimeField(label='Godzina zakończenia - poniedziałek', widget=TimeInput)
    tuesday_hour_start = forms.TimeField(label='Godzina rozpoczęcia - wtorek', widget=TimeInput)
    tuesday_hour_end = forms.TimeField(label='Godzina zakończenia - wtorek', widget=TimeInput)
    wednesday_hour_start = forms.TimeField(label='Godzina rozpoczęcia - środa', widget=TimeInput)
    wednesday_hour_end = forms.TimeField(label='Godzina zakończenia - środa', widget=TimeInput)
    thursday_hour_start = forms.TimeField(label='Godzina rozpoczęcia - czwartek', widget=TimeInput)
    thursday_hour_end = forms.TimeField(label='Godzina zakończenia - czwartek', widget=TimeInput)
    friday_hour_start = forms.TimeField(label='Godzina rozpoczęcia - piątek', widget=TimeInput)
    friday_hour_end = forms.TimeField(label='Godzina zakończenia - piątek', widget=TimeInput)
