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

    def clean(self):
        cleaned_data = super().clean()
        monday_hour_end = self.cleaned_data.get('monday_hour_end')
        monday_hour_start = cleaned_data.get('monday_hour_start')
        tuesday_hour_end = cleaned_data.get('tuesday_hour_end')
        tuesday_hour_start = cleaned_data.get('tuesday_hour_start')
        wednesday_hour_end = cleaned_data.get('wednesday_hour_end')
        wednesday_hour_start = cleaned_data.get('wednesday_hour_start')
        thursday_hour_end = cleaned_data.get('thursday_hour_end')
        thursday_hour_start = cleaned_data.get('thursday_hour_start')
        friday_hour_end = cleaned_data.get('friday_hour_end')
        friday_hour_start = cleaned_data.get('friday_hour_start')
        different_hours = cleaned_data.get('different_hours')

        if monday_hour_end is not None and monday_hour_start is None:
            self.add_error('monday_hour_start', 'Podaj początek pracy w poniedziałki')
        if monday_hour_start is not None and monday_hour_end is None:
            self.add_error('monday_hour_end', 'Podaj koniec pracy w poniedziałki')

        if tuesday_hour_end is not None and tuesday_hour_start is None:
            self.add_error('tuesday_hour_start', 'Podaj początek pracy we wtorki')
        if tuesday_hour_start is not None and tuesday_hour_end is None:
            self.add_error('tuesday_hour_end', 'Podaj koniec pracy we wtorki')

        if wednesday_hour_end is not None and wednesday_hour_start is None:
            self.add_error('wednesday_hour_start', 'Podaj początek pracy w środy')
        if wednesday_hour_start is not None and wednesday_hour_end is None:
            self.add_error('wednesday_hour_end', 'Podaj koniec pracy w środy')

        if thursday_hour_end is not None and thursday_hour_start is None:
            self.add_error('thursday_hour_start', 'Podaj początek pracy w czwartki')
        if thursday_hour_start is not None and thursday_hour_end is None:
            self.add_error('thursday_hour_end', 'Podaj koniec pracy w czwartki')

        if friday_hour_end is not None and friday_hour_start is None:
            self.add_error('friday_hour_start', 'Podaj początek pracy w piątki')
        if friday_hour_start is not None and friday_hour_end is None:
            self.add_error('friday_hour_end', 'Podaj koniec pracy w piątki')

        if different_hours == 'V':  # variable working hours
            if monday_hour_end is None and monday_hour_start is None:
                if tuesday_hour_end is None and tuesday_hour_start is None:
                    if wednesday_hour_end is None and wednesday_hour_start is None:
                        if thursday_hour_end is None and thursday_hour_start is None:
                            if friday_hour_end is None and friday_hour_start is None:
                                self.add_error('different_hours',
                                               'Podaj godziny w wybrane dni tygodnia, bądź wybierz opcję godzin stałych')
