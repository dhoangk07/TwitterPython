import tweepy
import config

def get_twitter_conn_v1() -> tweepy.API:
  auth = tweepy.OAuth1UserHandler(config.API_KEY, config.API_SECRET)
  auth.set_access_token(
    config.ACCESS_TOKEN,
    config.ACCESS_TOKEN_SECRET,
  )
  return tweepy.API(auth)

def get_twitter_conn_v2() -> tweepy.Client:
  client = tweepy.Client(consumer_key=config.API_KEY,
                         consumer_secret=config.API_SECRET,
                         access_token=config.ACCESS_TOKEN,
                         access_token_secret=config.ACCESS_TOKEN_SECRET)
  return client