import tweepy, string
import threading, cachetools

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
stopwords = {"a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "could", "did", "do", "does", "doing", "down", "during", "each", "few", "for", "from", "further", "had", "has", "have", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "it", "it's", "its", "itself", "let's", "me", "more", "most", "my", "myself", "nor", "of", "on", "once", "only", "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "she", "she'd", "she'll", "she's", "should", "so", "some", "such", "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "we", "we'd", "we'll", "we're", "we've", "were", "what", "what's", "when", "when's", "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "would", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves"}

queried_tweets = set()
for tweet in tweepy.Cursor(api.search, q=keyword, wait_on_rate_limit = True).items(10):
    text = str(tweet.text)
    text_as_list = text.lower().split()
    if "RT @" in text:
        text_as_list = (str(tweet.retweeted_status.text)).lower().split()
    without_stopwords = [word for word in text_as_list if word not in stopwords]
    polarity = get_polarity(tweet)


# Move to another python file
def get_polarity(clean_status):
    return 1


print(queried_tweets)

# Clean tweets
# Implement multithreads





# Analyze
