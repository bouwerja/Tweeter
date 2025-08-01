import tweepy
import settings as s

client = tweepy.Client(
    consumer_key=s.API,
    consumer_secret=s.API_SECRET,
    access_token=s.ACCESS,
    access_token_secret=s.ACCESS_SECRET
)

quotePost = """
Life is a shipwreck, but we must not forget to sing in the lifeboats.
"""
client.create_tweet(text=quotePost)