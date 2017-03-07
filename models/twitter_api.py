#!/usr/bin/python
# -*- coding: utf-8 -*-

import config

import tweepy
import pprint
pp = pprint.PrettyPrinter(indent=4)



class TwitterAPI:

    def __init__(self):
        consumer_key = config.consumer_key
        consumer_secret = config.consumer_secret
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = config.access_token
        access_token_secret = config.access_token_secret
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)


    def tweet(self, message):
        self.api.update_status(status=message)


    # TODO: These are mostly just testing methods, needs refactor

    def print_home_timeline(self):
        public_tweets = self.api.home_timeline()
        for tweet in public_tweets:
            print tweet.text


    def get_tweets_by_user(self, user):
        user_tweets = self.api.user_timeline(screen_name=user, count=100)
        for tweet in user_tweets:
            print tweet.text


    def get_tweets_by_user_mention(self, user):
        user_handle = '@' + user
        tweets = self.api.search(q=user_handle, count=100)
        for tweet in tweets:
            print tweet.text


    def get_reply_tweets(self):
        public_tweets = self.api.home_timeline()
        for tweet in public_tweets:
            # pp.pprint(tweet.__dict__.keys())
            try:
                print tweet.in_reply_to_status_id
            except:
                pass






