#!/usr/bin/python
# -*- coding: utf-8 -*-

# Quote scrape controller

import config

from models.quote import Quote

import requests
import json
import pprint
pp = pprint.PrettyPrinter(indent=4)



class QuoteScrape:


    @staticmethod
    def scrape_brainy():

        brainyquote_base_url = 'https://www.brainyquote.com'

        # make api call
        scrape_url = 'https://www.brainyquote.com/api/rand_q'
        res = requests.get(scrape_url)

        # process res data
        quote_data = json.loads(res.text)

        # create quote model instance
        quote = Quote.create(
            quote_text=quote_data['qt'].strip(),
            author=quote_data['an'],
            source_url=brainyquote_base_url + quote_data['q_url']
        )

        # store quote
        quote.save()


    @staticmethod
    def scrape_forismatic():

        # make api call
        scrape_url = 'http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en'
        res = requests.get(scrape_url)

        # process res data
        quote_data = json.loads(res.text)

        # create quote model instance
        quote = Quote.create(
            quote_text=quote_data['quoteText'].strip(),
            author=quote_data['quoteAuthor'],
            source_url=quote_data['quoteLink']
        )

        # store quote
        quote.save()


    @staticmethod
    def scrape_stands4():

        # make api call
        scrape_url = 'http://www.stands4.com/services/v2/quotes.php?'
        params = {
            'uid': config.stands4_id,
            'tokenid': config.stands4_token,
            'searchtype': 'RANDOM'
        }

        full_url = scrape_url + '&'.join(
            ['{0}={1}'.format(key, val) for key, val in params.iteritems()]
        )

        res = requests.get(full_url)

        pp.pprint(res.content)

        # process res data
        # create quote model instance
        # store quote










