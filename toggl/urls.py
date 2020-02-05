from django.urls import path

from toggl.views import index

urlpatterns = [
    path('', index),
]