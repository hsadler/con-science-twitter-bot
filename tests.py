#!/usr/bin/python
# -*- coding: utf-8 -*-

import pprint
pp = pprint.PrettyPrinter(indent=4)


from controllers.quote_scrape import QuoteScrape

QuoteScrape.scrape_brainy()
QuoteScrape.scrape_forismatic()
