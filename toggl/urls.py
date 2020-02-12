from django.urls import path

from toggl.views import index, done

urlpatterns = [
    path('', index, name='index'),
    path('done/', done),
]