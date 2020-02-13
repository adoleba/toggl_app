from django.urls import path

from toggl.views import done, EntryView

urlpatterns = [
    path('', EntryView.as_view(), name='index'),
    path('done/', done, name='done'),
]
