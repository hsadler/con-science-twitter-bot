#!/usr/bin/python
# -*- coding: utf-8 -*-

from controllers.quote_scrape import QuoteScrape


def scrape_brainy_and_forismatic():

	try:
		QuoteScrape.scrape_brainy()
	except:
		print 'brainy scrape fail'

	try:
		QuoteScrape.scrape_forismatic()
	except:
		print 'forismatic scrape fail'


def batch_scrape_stands4():

	QuoteScrape.batch_scrape_stands4(iterations=100, sleep_time=5)
