#!/usr/bin/python
# -*- coding: utf-8 -*-

# Quote scrape controller

from models.quote import Quote
from xml.etree import ElementTree

import config
import time
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
            author=quote_data['an'].strip(),
            source_url=brainyquote_base_url + quote_data['q_url'].strip()
        )

        # store quote
        quote.save()

        print '\nbrainy quote scrape success:'
        pp.pprint(quote.__dict__)


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
            author=quote_data['quoteAuthor'].strip(),
            source_url=quote_data['quoteLink'].strip()
        )

        # store quote
        quote.save()

        print '\nforismatic quote scrape success:'
        pp.pprint(quote.__dict__)


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

        # process res data
        res_tree = ElementTree.fromstring(res.content)

        quote_text = res_tree.find('result').find('quote').text
        quote_author = res_tree.find('result').find('author').text

        # create quote model instance
        quote = Quote.create(
            quote_text=quote_text.strip(),
            author=quote_author.strip()
        )

        # store quote
        quote.save()

        print '\nstands4 quote scrape success:'
        pp.pprint(quote.__dict__)


    @classmethod
    def batch_scrape_stands4(cls, iterations=100, sleep_time=5):

        for i in range(iterations):

            try:
                cls.scrape_stands4()
            except:
                print 'stantds4 scrape fail'

            time.sleep(sleep_time)










