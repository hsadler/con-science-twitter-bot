#!/usr/bin/python
# -*- coding: utf-8 -*-

import pprint
pp = pprint.PrettyPrinter(indent=4)



import bot

bot.scrape_brainy_and_forismatic()
bot.batch_scrape_stands4()

print 'testing complete...'


