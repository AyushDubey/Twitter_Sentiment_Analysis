# importing tweepy and textblob packages
import tweepy
from textblob import TextBlob

# twitter authentication
consumer_key = "lol"
consumer_secret = "lol"

access_token = "lol"
access_token_secret = "lol" 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search("Virat Kohli")

for tweet in public_tweets:
	print tweet.text
	analyze = TextBlob(tweet.text)
	print analyze.sentiment
