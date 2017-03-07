#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json

import pprint
pp = pprint.PrettyPrinter(indent=4)


# DEPRICATED: This is now an example file


class QuoteScraper:


    def scrape_brainy(self):

        scrape_url = 'https://www.brainyquote.com/api/rand_q'
        res = requests.get(scrape_url)

        new_quote = json.loads(res.text)
        quotes = None

        with open('test_quotes_scrape.json') as f:
            quotes = json.load(f)

        quotes.append(new_quote)

        with open('test_quotes_scrape.json', mode='w') as f:
            json.dump(quotes, f, indent=4)

    print 'brainy scrape complete...'


    def print_quote_file(self):

        with open('test_quotes_scrape.json') as f:
            quotes = json.load(f)
            pp.pprint(quotes)



scraper = QuoteScraper()
scraper.scrape_brainy()


