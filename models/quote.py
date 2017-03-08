#!/usr/bin/python
# -*- coding: utf-8 -*-

# Quote model

from models.database import MySQL_DB

import hashlib
import pprint
pp = pprint.PrettyPrinter(indent=4)



class Quote:


    def __init__(self, quote_text, author, source_url, active, md5hash):
        
        # CREATE TABLE IF NOT EXISTS quotes(
        #     id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
        #     quote_text VARCHAR(2000) NOT NULL,
        #     author VARCHAR(255),
        #     source_url VARCHAR(1000),
        #     active TINYINT(1) DEFAULT 1 NOT NULL,
        #     md5hash VARCHAR(32)
        #     UNIQUE (md5hash)
        # );

        self.quote_text = quote_text
        self.author = author
        self.source_url = source_url
        self.active = active
        self.md5hash = md5hash


    # create instance from gathered data
    @classmethod
    def create(cls, quote_text, author=None, source_url=None, active=1):
        
        return cls(
            quote_text = quote_text,
            author = author,
            source_url = source_url,
            active = active,
            md5hash = hashlib.md5(quote_text.encode('ascii', 'ignore')).hexdigest()
        )


    def save(self):

        db = MySQL_DB()

        with db.connection:
            
            query = """
                INSERT INTO quotes(quote_text, author, source_url, active, md5hash) 
                VALUES(%s, %s, %s, %s, %s);
            """

            data = (
                self.quote_text,
                self.author,
                self.source_url,
                self.active,
                self.md5hash
            )

            db.cur.execute(query, data)

            db.cur.execute('SELECT LAST_INSERT_ID();')
            self.id = db.cur.fetchone()['LAST_INSERT_ID()']

        return self


    def find_by_quote_text(self):
        pass


    def update(self):
        pass


    def delete(self):
        pass


