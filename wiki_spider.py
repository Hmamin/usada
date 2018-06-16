# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 21:49:57 2018

@author: Harrison Mamin
"""

import scrapy

class FighterWiki(scrapy.Spider):
    '''Scrape fighters' Wikipedia pages for w/l record, weight class,
    league, etc.'''
    
    name = 'fighters'
    
    def start_requests(self):
    