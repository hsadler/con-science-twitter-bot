#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb


con = mdb.connect('localhost', 'root', '', 'con_science_bot')
cur = con.cursor()

with con:

    # cur.execute('DROP TABLE quotes;')

    # create quotes table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS quotes(
        id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
        quote_text VARCHAR(2000) NOT NULL,
        author VARCHAR(255),
        source_url VARCHAR(1000),
        active TINYINT(1) DEFAULT 1 NOT NULL,
        md5hash VARCHAR(32) NOT NULL);
    """)



