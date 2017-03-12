#!/usr/bin/python
# -*- coding: utf-8 -*-

# Error Log model

import logging
logger = logging.getLogger('con_science_bot')
hdlr = logging.FileHandler('logs/error.log')
formatter = logging.Formatter('\n%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)

import pprint
pp = pprint.PrettyPrinter(indent=4)



class ErrorLog:


    def __init__(self, message):
        self.message = message


    # create instance from error
    @classmethod
    def log_exception(cls, message):
        exception = cls(message=message)
        logger.exception(exception.message)
        return exception


    # test the logger
    @classmethod
    def test_error(cls):
        try:
            1/0
        except:
            error_message = 'i am a test error message'
            error = cls.log_exception(error_message)






