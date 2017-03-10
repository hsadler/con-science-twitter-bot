#!/usr/bin/python
# -*- coding: utf-8 -*-

# Quote scrape controller

import config

import requests
import json

import pprint
pp = pprint.PrettyPrinter(indent=4)



class QuoteScrape:


    @staticmethod
    def scrape_brainy():

        # make api call
        scrape_url = 'https://www.brainyquote.com/api/rand_q'
        res = requests.get(scrape_url)

        new_quote = json.loads(res.text)
        
        pp.pprint(new_quote)
        
        # process res data
        # create quote model instance
        # store quote
        


    @staticmethod
    def scrape_forismatic():
        
        # make api call
        scrape_url = 'http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en'
        res = requests.get(scrape_url)

        new_quote = json.loads(res.text)
        
        pp.pprint(new_quote)
        
        # process res data
        # create quote model instance
        # store quote


    @staticmethod
    def scrape_stands4():
        
        # make api call
        scrape_url = 'http://www.stands4.com/services/v2/quotes.php?uid=[user_id]&tokenid=[user_token]&searchtype=SEARCH'
        params = {
            'uid': config.stands4_uid,
            'tokenid': config.stands4_tokenid,
            'searchtype': 'SEARCH'
        }
        res = requests.get(scrape_url)

        new_quote = json.loads(res.text)
        
        pp.pprint(new_quote.__dict__)
        
        # process res data
        # create quote model instance
        # store quote



