from datetime import timedelta

import requests
from django.http import HttpResponse
from django.shortcuts import render

from toggl.forms import EntryForm

headers = {
    "Authorization": "",
    "Content-Type": "application/json",
    "Accept": "*/*",
    "User-Agent": "python/urllib",
}


def index(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)

        if form.is_valid():
            working_days = []
            week_days = {}

            date_start = form.cleaned_data['date_start']
            date_end = form.cleaned_data['date_end']
            hour_start = form.cleaned_data['hour_start']
            hour_end = form.cleaned_data['hour_end']

            task = form.cleaned_data['task']
            toggl_login = form.cleaned_data['toggl_login']
            toggl_id_number = form.cleaned_data['toggl_id_number']
            toggl_password = form.cleaned_data['toggl_password']

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

            return HttpResponse('Dodano')

    else:
        form = EntryForm(request.POST)

    return render(request, 'toggl/index.html', {'form': form})

