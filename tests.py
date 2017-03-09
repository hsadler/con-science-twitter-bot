#!/usr/bin/python
# -*- coding: utf-8 -*-

from models.quote import Quote
import pprint
pp = pprint.PrettyPrinter(indent=4)



try:
	quote = Quote.create('I am a banana!')
	quote.save()
	pp.pprint(quote.__dict__)
except:
	print 'got nothing...'




