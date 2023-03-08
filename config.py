import os
import tweepy
from dotenv import load_dotenv

load_dotenv()

def connect_api():
    consumer_key = os.getenv('API_KEY')
    consumer_secret= os.getenv('API_SECRET')
    access_token = os.getenv('ACCESS_TOKEN') 
    access_secret= os.getenv('ACCESS_SECRET')

    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_secret)
    api = tweepy.API(auth)
    return api