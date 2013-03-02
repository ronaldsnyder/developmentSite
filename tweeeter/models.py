from django.db import models

class PythonTweets(models.Model):
    tweetUsr = models.CharField(max_length=200)
    tweetText = models.CharField(max_length=500)
    tweetUrl = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    