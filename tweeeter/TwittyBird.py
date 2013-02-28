#TwittyBird.py 
#Written By Ron Snyder
#Purpose:  Get Tweets from Twitter to insert into database.
#to do open twitter and get tweets.
#read json feed
#insert into database.
import urllib2
import json
import sqlite3

debug = False
twitter_search = 'http://search.twitter.com/search.json?q=Python&rpp=1&result_type=mixed&lang=en'
response = urllib2.urlopen(twitter_search)
json_feed = json.load(response)

#setup DB
conn = sqlite3.connect('sqlite.db')
c = conn.cursor()
#c.execute ('''CREATE TABLE tweets (user text, tweet text, url text)''')

if debug:
    json_string = json.dumps(json_feed,sort_keys=True,indent=2)
    print json_string
#parent = json_feed["results"]
#for item in parent:
    #c.execute('INSERT INTO tweeeter_pythontweets VALUES (? , ?, ?)', ((item["from_user"]), 
  #                                                     (item["from_user"] + ": " + item["text"]), 
   #                                                    ('https://twitter.com/' + item["from_user"] + 
   #                                                     '/status/' + str(item["id"]))))
if debug:
    print 'database row print'
    for row in c.execute('SELECT * from tweets'):
        print row
for row in c.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"):
    print row