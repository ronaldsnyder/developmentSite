# Create your views here.
from django.shortcuts import render_to_response
from tweeeter.models import PythonTweets

def python_search(request):
    latest_python_tweets = PythonTweets.objects.all().order_by('-pub_date')
    return render_to_response('tweeeter/python.html', {'latest_python_tweets': latest_python_tweets})
