#TwittyBird.py 
#Written By Ron Snyder
#Purpose:  Get Tweets from Twitter to insert into database.
import urllib2
import json
from tweeeter.models import PythonTweets, HomeTownTweets
from time import gmtime, strftime

def grab_some_tweets(obj, twitter_search):
    response = urllib2.urlopen(twitter_search)
    json_feed = json.load(response)
    parent = json_feed["results"]
    for item in parent:
        print item
        rds = obj(
        tweetUsr = (item["from_user"]),
        tweetText = (item["text"]),
        tweetUrl = ('https://twitter.com/' + item["from_user"] + '/status/' + str(item["id"])),
        pub_date = todays_date)
        rds.save()    

# setup pythonTweets
PythonTweets.objects.all().delete()
todays_date = strftime('%Y-%m-%d %H:%M:%S', gmtime())
#change below to customize the results
search_term = 'python+programming'
search_count= '50'
twitter_search = 'http://search.twitter.com/search.json?q=' + search_term + '&rpp=' + search_count + '&result_type=mixed&lang=en'
#get the tweets for pthon programming
grab_some_tweets(PythonTweets, twitter_search)
    
# setup homeTownTweets
HomeTownTweets.objects.all().delete()
todays_date = strftime('%Y-%m-%d %H:%M:%S', gmtime())
#change below to customize the results
search_count= '50'
twitter_search = 'http://search.twitter.com/search.json?geocode=42.7978,-83.7050,5mi&rpp=' + search_count + '&result_type=mixed&lang=en'
print twitter_search
#get the tweets for pthon programming
grab_some_tweets(HomeTownTweets, twitter_search)
