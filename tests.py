#!/usr/bin/python
# -*- coding: utf-8 -*-

from models.twitter_api import TwitterAPI


twitter = TwitterAPI()
twitter.get_tweets_by_user('codeharry')