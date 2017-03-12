#!/usr/bin/python
# -*- coding: utf-8 -*-

from models.error_log import ErrorLog
from controllers.quote_scrape import QuoteScrape



def scrape_brainy_and_forismatic():

	try:
		QuoteScrape.scrape_brainy()
	except:
        ErrorLog.log_exception('brainy scrape fail')

	try:
		QuoteScrape.scrape_forismatic()
	except:
        ErrorLog.log_exception('forismatic scrape fail')


def batch_scrape_stands4():

	QuoteScrape.batch_scrape_stands4(iterations=100, sleep_time=5)
