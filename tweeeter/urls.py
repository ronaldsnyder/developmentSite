from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from tweeeter.models import PythonTweets
import tweeeter.views 

urlpatterns = patterns('',
    (r'^python', 'tweeeter.views.python_search'),
    )