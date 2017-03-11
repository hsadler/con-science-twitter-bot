#!/usr/bin/python
# -*- coding: utf-8 -*-

# Error Log model

import pprint
pp = pprint.PrettyPrinter(indent=4)



class ErrorLog:


    def __init__(self, error):
        self.error = error


    # create instance from gathered data
    @classmethod
    def create(cls, error):
        return cls(error=error)


    # write error log to file
    def write(self):
        return self








