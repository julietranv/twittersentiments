import tweepy, string
import threading, cachetools
from util import *

# Variables that contains the user credentials to access Twitter API
CONSUMER_KEY = "xlr2nyxR92LYzpEC5Q9zuc4Sn"
CONSUMER_SECRET = "qroJJ6jSEKAqvWImNAcexxxMEAsLFOMQdfIzcY5GI5vmOqqFot"
ACCESS_TOKEN = "1081691069652205568-V9Vw50VOEUnimHjLtSay7107JWqlad"
ACCESS_SECRET = "tykzoeiCQh6KKGA1MCLSExmfvwGt2xuVqPvfPmgT3WHcQ"

# Setup tweepy to authenticate with Twitter credentials:
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

# Will implement user input
keyword = "Donald"

for tweet in tweepy.Cursor(api.search, q=keyword, wait_on_rate_limit = True).items(10):
    parsed = clean_tweet(tweet)


# Implement multithreads





# Analyze
