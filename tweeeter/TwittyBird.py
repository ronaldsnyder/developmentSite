#TwittyBird.py 
#Written By Ron Snyder
#Purpose:  Get Tweets from Twitter to insert into database.
import urllib2
import json
from tweeeter.models import PythonTweets
from time import gmtime, strftime

PythonTweets.objects.all().delete()
todays_date = strftime('%Y-%m-%d %H:%M:%S', gmtime())

#change below to customize the results
search_term = 'python+programming'
search_count= '50'
twitter_search = 'http://search.twitter.com/search.json?q=' + search_term + '&rpp=' + search_count + '&result_type=mixed&lang=en'

#open twitter and get what you want.
response = urllib2.urlopen(twitter_search)
json_feed = json.load(response)

#cycle through tweets, create objects and save.  
parent = json_feed["results"]
for item in parent:
    print item
    rds = PythonTweets(
    tweetUsr = (item["from_user"]),
    tweetText = (item["text"]),
    tweetUrl = ('https://twitter.com/' + item["from_user"] + '/status/' + str(item["id"])),
    pub_date = todays_date)
    rds.save()