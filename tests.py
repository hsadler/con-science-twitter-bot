#!/usr/bin/python
# -*- coding: utf-8 -*-

import pprint
pp = pprint.PrettyPrinter(indent=4)


# from controllers.quote_scrape import QuoteScrape

# QuoteScrape.scrape_brainy()
# QuoteScrape.scrape_forismatic()


from models.twitter_api import TwitterAPI
import time

twitter = TwitterAPI()

# print '\n========================================\n'

# users_tweets = twitter.get_tweets_by_user(user='FoxNews')
# pp.pprint(users_tweets[0].__dict__)

# time.sleep(2)


print '\n++++++++++++++++++++++++++++++++++++++++\n'

mention_tweets = twitter.get_tweets_by_user_mention(user='FoxNews')

ids = []
for tweet in mention_tweets:
    if tweet.in_reply_to_status_id is not None:
        print tweet.in_reply_to_status_id


# time.sleep(2)


# print '\n-----------------------------------------\n'

# orig_tweets = twitter.get_tweets_by_ids(ids=ids)

















