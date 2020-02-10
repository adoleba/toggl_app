from datetime import timedelta

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from toggl.forms import EntryForm


def index(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)

        if form.is_valid():
            working_days = []
            week_days = {}

            date_start = form.cleaned_data['date_start']
            date_end = form.cleaned_data['date_end']

            week_days['first_monday'] = date_start + timedelta(days=0 - date_start.weekday())
            week_days['first_tuesday'] = date_start + timedelta(days=1 - date_start.weekday())
            week_days['first_wednesday'] = date_start + timedelta(days=2 - date_start.weekday())
            week_days['first_thursday'] = date_start + timedelta(days=3 - date_start.weekday())
            week_days['first_friday'] = date_start + timedelta(days=4 - date_start.weekday())

            for day in week_days:
                date = week_days[day]
                if week_days[day] >= date_start:
                    working_days.append(date)
                next_day = date + timedelta(days=7)
                while next_day <= date_end:
                    working_days.append(next_day)
                    next_day += timedelta(days=7)

            return HttpResponseRedirect('/')

    else:
        form = EntryForm(request.POST)

    return render(request, 'toggl/index.html', {'form': form})

