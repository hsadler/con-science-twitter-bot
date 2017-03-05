#!/usr/bin/python
# -*- coding: utf-8 -*-

from models.twitter_api import TwitterAPI


twitter = TwitterAPI()
twitter.print_home_timeline()
