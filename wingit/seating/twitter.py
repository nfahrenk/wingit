import tweepy
from tweepy import OAuthHandler
import datetime as dt
from datetime import timedelta
import urllib2
import urllib
import sys
import base64
import json

consumer_key = '0xu5sVlH9fUNp7WZGdE6nuSBy'
consumer_secret = 'bYsmKLrzDRfZ47noeRsaaFEiEdFFAe8vaSb5BueGBt0O96lPmJ'
access_token = '779782417926217728-El9F48CPfdgQe6fafvibR0c8d0NPWUr'
access_secret = 'vIDC6eLgaCHuzv0IeybfGtsFbR4jrUhBvTmbyZTdGrIEq'



class twitter():

    @staticmethod
    def getRecentTweets(twitter_name):

        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)

        api = tweepy.API(auth)


        alltweets = []
        count = 1
        tweets = api.user_timeline(screen_name = twitter_name, count = 1)
        alltweets.extend(tweets)
        oldest = alltweets[-1].id - 1
        stringTweets = '{"documents":[{"id":"%d","text":"%s"}' % (count, alltweets[-1].text.encode('ascii', errors='backslashreplace'))

        one_day = timedelta(days=1)
        yesterday = dt.datetime.today() - one_day

        boo = alltweets[-1].created_at > yesterday


        while boo and len(tweets) > 0:

            tweets = api.user_timeline(screen_name = twitter_name, count=1, max_id=oldest)


            alltweets.extend(tweets)
            oldest = alltweets[-1].id - 1

            boo = alltweets[-1].created_at > yesterday


            count = count + 1

            if boo and len(tweets) > 0:
                stringTweets = stringTweets + ',{"id":"%d","text":"%s"}' % (count, alltweets[-1].text)

        stringTweets = stringTweets + ']}'
        
        return str(stringTweets)



    @staticmethod
    def getSentiment(input_tweets):
        url = 'https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment'

        account_key = '0a3709dd6e294540bdbe1d3747702c5e'

        headers = {'Content-Type':'application/json', 'Ocp-Apim-Subscription-Key':account_key}

        num_detect_langs = 1;

        req = urllib2.Request(url, input_tweets, headers)
        response = urllib2.urlopen(req)
        result = response.read()
        obj = json.loads(result)

        count = 0.0
        total = 0.0
        for sentiment_analysis in obj['documents']:
            total = total + float(str(sentiment_analysis['score']))
            count = count + 1

        return total / count
