from datetime import timedelta

import requests
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from toggl.forms import EntryForm

headers = {
    "Authorization": "",
    "Content-Type": "application/json",
    "Accept": "*/*",
    "User-Agent": "python/urllib",
}


class EntryView(FormView):
    form_class = EntryForm
    template_name = 'toggl/index.html'
    success_url = reverse_lazy('done')

    def form_valid(self, form):
        add_toggl_entry(form.cleaned_data)
        return super().form_valid(form)


def add_toggl_entry(valid_data):
    different_hours = valid_data['different_hours']
    date_start = valid_data['date_start']
    date_end = valid_data['date_end']
    task = valid_data['task']
    toggl_login = valid_data['toggl_login']
    toggl_id_number = valid_data['toggl_id_number']
    toggl_password = valid_data['toggl_password']

    if different_hours == 'R':  # regular, choice from form choices
        working_days = []
        week_days = {}

        hour_start = valid_data['hour_start']
        hour_end = valid_data['hour_end']

        week_days['first_monday'] = date_start + timedelta(days=0 - date_start.weekday())
        week_days['first_tuesday'] = date_start + timedelta(days=1 - date_start.weekday())
        week_days['first_wednesday'] = date_start + timedelta(days=2 - date_start.weekday())
        week_days['first_thursday'] = date_start + timedelta(days=3 - date_start.weekday())
        week_days['first_friday'] = date_start + timedelta(days=4 - date_start.weekday())

        duration_in_sec = (hour_end.hour - hour_start.hour) * 3600

        for day in week_days:
            date = week_days[day]
            if week_days[day] >= date_start:
                working_days.append(date)
            next_day = date + timedelta(days=7)
            while next_day <= date_end:
                working_days.append(next_day)
                next_day += timedelta(days=7)

        for day in working_days:
            data = {
                "time_entry": {
                    "description": task,
                    "duration": str(duration_in_sec),
                    "start": str('{:04d}'.format(day.year)) + "-" + str('{:02d}'.format(day.month)) + "-" + str(
                        '{:02d}'.format(day.day)) + "T" + str('{:02d}'.format(hour_start.hour - 1)) + ":" + str(
                        '{:02d}'.format(hour_start.minute)) + ":00.000Z",
                    "id": toggl_id_number,
                    "created_with": "curl",
                }
            }
            resp = requests.post(
                'https://www.toggl.com/api/v8/time_entries',
                auth=(toggl_login, toggl_password),
                json=data,
                headers=headers,
            )

    else:

        week_days = {}
        working_days = {}

        monday_hour_start = valid_data['monday_hour_start']
        monday_hour_end = valid_data['monday_hour_end']
        tuesday_hour_start = valid_data['tuesday_hour_start']
        tuesday_hour_end = valid_data['tuesday_hour_end']
        wednesday_hour_start = valid_data['wednesday_hour_start']
        wednesday_hour_end = valid_data['wednesday_hour_end']
        thursday_hour_start = valid_data['thursday_hour_start']
        thursday_hour_end = valid_data['thursday_hour_end']
        friday_hour_start = valid_data['friday_hour_start']
        friday_hour_end = valid_data['friday_hour_end']

        if monday_hour_start and monday_hour_end is not None:
            week_days['first_monday'] = [date_start + timedelta(days=0 - date_start.weekday()),
                                         monday_hour_start,
                                         (monday_hour_end.hour - monday_hour_start.hour) * 3600]

        if tuesday_hour_start and tuesday_hour_end is not None:
            week_days['first_tuesday'] = [date_start + timedelta(days=1 - date_start.weekday()),
                                          tuesday_hour_start,
                                          (tuesday_hour_end.hour - tuesday_hour_start.hour) * 3600]

        if wednesday_hour_start and wednesday_hour_end is not None:
            week_days['first_wednesday'] = [date_start + timedelta(days=2 - date_start.weekday()),
                                            wednesday_hour_start,
                                            (wednesday_hour_end.hour - wednesday_hour_start.hour) * 3600]

        if thursday_hour_start and thursday_hour_end is not None:
            week_days['first_thursday'] = [date_start + timedelta(days=3 - date_start.weekday()),
                                           thursday_hour_start,
                                           (thursday_hour_end.hour - thursday_hour_start.hour) * 3600]

        if friday_hour_start and friday_hour_end is not None:
            week_days['first_friday'] = [date_start + timedelta(days=4 - date_start.weekday()),
                                         friday_hour_start,
                                         (friday_hour_end.hour - friday_hour_start.hour) * 3600]

        for day in week_days:
            date = week_days[day][0]

            if date >= date_start:
                # date, start hour, duration in sec
                working_days[date] = [date, week_days[day][1], week_days[day][2]]
            next_day = date + timedelta(days=7)
            while next_day <= date_end:
                working_days[next_day] = [next_day, week_days[day][1], week_days[day][2]]
                next_day += timedelta(days=7)

        for day in working_days:
            time = working_days[day][1]
            data = {
                "time_entry": {
                    "description": task,
                    "duration": str(working_days[day][2]),
                    "start": str('{:04d}'.format(day.year)) + "-" + str('{:02d}'.format(day.month)) + "-" + str(
                        '{:02d}'.format(day.day)) + "T" + str('{:02d}'.format(time.hour - 1)) + ":" + str(
                        '{:02d}'.format(time.minute)) + ":00.000Z",
                    "id": toggl_id_number,
                    "created_with": "curl",
                }
            }
            resp = requests.post(
                'https://www.toggl.com/api/v8/time_entries',
                auth=(toggl_login, toggl_password),
                json=data,
                headers=headers,
            )


def done(request):
    return render(request, 'toggl/done.html')
