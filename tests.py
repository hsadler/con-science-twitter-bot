#!/usr/bin/python
# -*- coding: utf-8 -*-

from models.quote import Quote
import pprint
pp = pprint.PrettyPrinter(indent=4)



# try:
# 	quote = Quote.create('I am a banana!')
# 	quote.save()
# 	pp.pprint(quote.__dict__)
# except:
# 	print 'insert already exists'


# fetched_quote = Quote.find_by_quote_text('I am a banana!')
# if fetched_quote is not None:
#     pp.pprint(fetched_quote.__dict__)


from controllers.quote_scrape import QuoteScrape

# QuoteScrape.scrape_brainy()
QuoteScrape.scrape_forismatic()
# QuoteScrape.scrape_stands4()
