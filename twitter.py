import os
from TwitterAPI import TwitterAPI


class Twitter(object):
    def __init__(self):
        consumer_key = os.environ.get('twitter_consumer_key')
        consumer_secret = os.environ.get('twitter_consumer_secret')
        access_token_key = os.environ.get('twitter_access_token_key')
        access_token_secret = os.environ.get('twitter_access_token_secret')
        self.api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

    def post_image(self, filename):

        file = open(filename, 'rb')
        data = file.read()
        r = self.api.request('media/upload', None, {'media': data})

        if r.status_code == 200:
            media_id = r.json()['media_id']
            r = self.api.request('statuses/update', {'status': '', 'media_ids': media_id})

        return r
