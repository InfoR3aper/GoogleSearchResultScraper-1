# -*- coding: utf-8 -*-
import scrapy

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
sys.path.insert(0, os.path.dirname(os.path.dirname(parent_dir)))

from searchResults import getResultsURL

class TestSpider(scrapy.Spider):
	print("===============")
	print(getResultsURL())
	print("===============")
	name = 'test'
	allowed_domains = ['google.com']
	start_urls = ['http://google.com/']

	def parse(self, response):
		pass
