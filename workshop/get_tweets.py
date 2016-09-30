#Import some methods from tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#User credentials to access the Twitter API 
access_token = "234259217-wTGAV5iUiwCTHA3rMI9XSeonvrpvIAWnWjBdApmx"
access_token_secret = "06l14RLMBnNQZC8XiMPuJDQQakNIZ6JJOOR3NhWhabQfq"
consumer_key = "lTc4xMb2T0JhKqkaNmNvDdow2"
consumer_secret = "CUhLv2EkbkdxTz4o6uDRQpeaOuEv1huqRoPaDNvwye14xrl7Qr"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #The filter Twitter Streams to capture data by the keywords:
    stream.filter(track=['modi', 'kejriwal'])            