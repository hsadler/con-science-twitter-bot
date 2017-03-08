#!/usr/bin/python
# -*- coding: utf-8 -*-

# Quote model

from models.database.database import MySQL_DB

import hashlib
import pprint
pp = pprint.PrettyPrinter(indent=4)



class Quote:


    def __init__(self, quote_text, author, source_url=None, active=1):
        # CREATE TABLE IF NOT EXISTS quotes(
        # id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
        # quote_text VARCHAR(2000) NOT NULL,
        # author VARCHAR(255),
        # source_url VARCHAR(1000),
        # active TINYINT(1) DEFAULT 1 NOT NULL,
        # md5hash VARCHAR(32) NOT NULL);
        self.quote_text = quote_text
        self.author = author
        self.source_url = source_url
        self.active = active


    def create(self):
        pass


    def find(self):
        pass


    def update(self):
        pass


    def delete(self):
        pass


