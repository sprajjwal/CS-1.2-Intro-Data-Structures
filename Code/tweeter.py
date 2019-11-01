import os
import tweepy as tw

def tweet(msg):
    """TWEETS THE MESSAGE TO THE TWITTER ACCOUNT"""
    consumer_key = os.environ['CONSUMER_KEY'] 
    consumer_secret = os.environ['CONSUMER_SECRET']
    access_token = os.environ['ACCESS_TOKEN']
    access_token_secret = os.environ['ACCESS_TOKEN_SECRET']
    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)
    api.update_status(msg)
