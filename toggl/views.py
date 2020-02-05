from django.shortcuts import render
from toggl.forms import EntryForm


def index(request):
    form = EntryForm()
    return render(request, 'toggl/index.html', {'form': form})

