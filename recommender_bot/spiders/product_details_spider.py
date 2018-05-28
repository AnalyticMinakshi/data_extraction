# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 17:32:21 2018

@author: Minu
"""

import scrapy
import logging
from recommender_bot.items import ProductCategoryItem
from urllib.parse import urlparse
import json
import pkgutil
import sys

logging.basicConfig(filename='product_details.log', level=logging.DEBUG)
logger = logging.getLogger('mycustomlogger')
client_config_info = json.loads(pkgutil.get_data("recommender_bot", "resources/client_config.json"))

class ProductDetailsSpider(scrapy.Spider):
	name = "productdetailsspider"
	allowed_domain = client_config_info['allowed_domain']
	start_urls = client_config_info['start_urls']
    
	def parse(self, response):
		try:
			for k,v in client_config_info['client_config'].items():
				if(k=="grofers_configuration"):
					category_urls = response.xpath(v['category_urls']).extract()
					category_counter = 1
					for category_url in category_urls:
						if(category_counter <= len(category_urls)): #len(category_urls)
							category_name = response.xpath(v['items']['category_name'] % str(category_counter)).extract()             
							category_url_absolute = response.urljoin(category_url)     
							yield scrapy.Request(category_url_absolute, callback = self.parse_indetail, meta = {'category_name' : category_name, 'x_items_list' : v['items_list'], 
																												'x_item_name': v['items']['item_name'], 'x_quantity': v['items']['quantity'],
																												'x_price': v['items']['price'], 'x_offer': v['items']['offer'],
																												'x_old_price': v['items']['old_price']})                    
						category_counter = category_counter + 1
		except:
			print("ProductDetailsSpider: parse: ", sys.exc_info()[0])
			raise
        
	def parse_indetail(self, response):
		try:
			#page = 1   
			item_counter = 1
			self.logger.info('@@@@@@@@@@@@@@@@@ %s @@@@@@@@@@@@@@', response.url)
			items = response.xpath(response.meta['x_items_list']).extract()
			for item in items:
				if(item_counter <= len(items)):
					pc_item = ProductCategoryItem()
					pc_item['item_id'] = item_counter
					pc_item['category_name'] = response.meta['category_name']
					pc_item['category_reference'] = response.url
					pc_item['item_name'] = response.xpath(response.meta['x_item_name'] % str(item_counter)).extract()                 
					pc_item['quantity'] = response.xpath(response.meta['x_quantity'] % str(item_counter)).extract()
					pc_item['price'] = response.xpath(response.meta['x_price'] % str(item_counter)).extract()
					pc_item['offer']  = response.xpath(response.meta['x_offer'] % str(item_counter)).extract()
					pc_item['old_price'] = response.xpath(response.meta['x_old_price'] % str(item_counter)).extract() 
					yield pc_item
				item_counter = item_counter + 1
			#o = urlparse(response.url)
			#self.page += 1
			#next_page = o.path + "?page=" + str(self.page)
			#if len(items) == 48:
				#yield scrapy.Request(response.urljoin(next_page), self.parse_indetail, meta = {'category_name': response.meta['category_name']})
		except:
			print("ProductDetailsSpider: parse_indetail: ", sys.exc_info()[0])
			raise	
